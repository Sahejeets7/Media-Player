from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import uic
from PyQt5.uic import loadUiType
# from pyqt5down1 import MainApp
from index import MainApp
from browser_tabbed import Browser
from wordprocessor import ProcessorWindow

# from PyQt5.QtWebEngineWidgets import *


from random import shuffle
# import pickle

# from gui import Ui_MainWindow
import os
from os import path
import sys

# import UI File to use it in the next class that runs the GUI in pycharm
# when you make change in Qt designer it change automatic here
FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "gui1.ui"))




# class ViewerWindow(QMainWindow):
#     state = pyqtSignal(bool)

#     def closeEvent(self, e):
#         self.hide()
#         # Emit the window state, to update the viewer toggle button.
#         # self.state.emit(False)

#{#####################################################################################################

class PlaylistModel(QAbstractItemModel):

    Title, ColumnCount = range(2)

    def __init__(self, parent=None):
        super(PlaylistModel, self).__init__(parent)                         
 
        self.m_playlist = None

    def rowCount(self, parent=QModelIndex()):
        return self.m_playlist.mediaCount() if self.m_playlist is not None and not parent.isValid() else 0

    def columnCount(self, parent=QModelIndex()):
        return self.ColumnCount if not parent.isValid() else 0

    def index(self, row, column, parent=QModelIndex()):
        return self.createIndex(row, column) if self.m_playlist is not None and not parent.isValid() and row >= 0 and row < self.m_playlist.mediaCount() and column >= 0 and column < self.ColumnCount else QModelIndex()

    def parent(self, child):
        return QModelIndex()

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.DisplayRole:
            if index.column() == self.Title:
                location = self.m_playlist.media(index.row()).canonicalUrl()
                return QFileInfo(location.path()).fileName()

            return self.m_data[index]

        return None

    def playlist(self):
        return self.m_playlist

    def setPlaylist(self, playlist):
        if self.m_playlist is not None:
            self.m_playlist.mediaAboutToBeInserted.disconnect(
                    self.beginInsertItems)
            self.m_playlist.mediaInserted.disconnect(self.endInsertItems)
            self.m_playlist.mediaAboutToBeRemoved.disconnect(
                    self.beginRemoveItems)
            self.m_playlist.mediaRemoved.disconnect(self.endRemoveItems)
            self.m_playlist.mediaChanged.disconnect(self.changeItems)

        self.beginResetModel()
        self.m_playlist = playlist

        if self.m_playlist is not None:
            self.m_playlist.mediaAboutToBeInserted.connect(
                    self.beginInsertItems)
            self.m_playlist.mediaInserted.connect(self.endInsertItems)
            self.m_playlist.mediaAboutToBeRemoved.connect(
                    self.beginRemoveItems)
            self.m_playlist.mediaRemoved.connect(self.endRemoveItems)
            self.m_playlist.mediaChanged.connect(self.changeItems)

        self.endResetModel()

    def beginInsertItems(self, start, end):
        self.beginInsertRows(QModelIndex(), start, end)

    def endInsertItems(self):
        self.endInsertRows()

    def beginRemoveItems(self, start, end):
        self.beginRemoveRows(QModelIndex(), start, end)

    def endRemoveItems(self):
        self.endRemoveRows()

    def changeItems(self, start, end):
        self.dataChanged.emit(self.index(start, 0),                            
                self.index(end, self.ColumnCount))



#}##################################################################################


class MainWindow(QMainWindow, FORM_CLASS):

    changeRate = pyqtSignal(float)
    changeMuting = pyqtSignal(bool)

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # uic.loadUi("gui1.ui", self)

        self.setupUi(self)


        # self.player = QMediaPlayer()

        # self.player.error.connect(self.erroralert)
        # self.player.play()

        # widget = Qvideo()
        # # self.viewer.setCentralWidget(video)
        # self.player.setVideoOutput(widget)
        # self.open_file_action.triggered.connect(self.open_files)


#{#####################################################################################################
    
        self.playlistSet = set()
        self.play_list = []

    # fullScreenChanged = pyqtSignal(bool)

    # def __init__(self, playlist, parent=None):
    #     super(Player, self).__init__(parent)

    

        self.colorDialog = None
        self.trackInfo = ""
        self.statusInfo = ""
        self.duration = 0

        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)

        self.player.error.connect(self.erroralert)

        self.player.durationChanged.connect(self.durationChanged)
        self.player.positionChanged.connect(self.positionChanged)
        # self.player.metaDataChanged.connect(self.metaDataChanged)
        self.playlist.currentIndexChanged.connect(self.playlistPositionChanged)
        self.player.mediaStatusChanged.connect(self.statusChanged)
        self.player.bufferStatusChanged.connect(self.bufferingProgress)
        self.player.videoAvailableChanged.connect(self.videoAvailableChanged)
        self.player.error.connect(self.displayErrorMessage)

        self.player.setVideoOutput(self.video)

        self.video.setStyleSheet("background-color: black")

        self.playlistModel = PlaylistModel()
        self.playlistModel.setPlaylist(self.playlist)

        # self.playlistView = QListView()
        # self.model = PlaylistModel(self.playlist)
        self.playlistView.setModel(self.playlistModel)
        self.playlistView.setCurrentIndex(
                self.playlistModel.index(self.playlist.currentIndex(), 0))
        ####
        # self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        # self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemOnce)
        # self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        # self.playlist.setPlaybackMode(QMediaPlaylist.Random)

        #custom right-click event
        self.right = False
        self.playlistView.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.playlistView.clicked.connect(self.playlistView, SIGNAL("customContextMenuRequested(QPoint)"), self.on_playlistView_clicked)


        # Create a menu
        # self.menu = QtWidgets.QMenu("Menu", self)
        # self.actionMetaData = QAction("Show Media Info", self.playlistView)
        # self.actionDelete = QAction("Delete", self.playlistView)
        # self.menu.addAction(self.actionMetaData)
        # menu.addAction(self.mAction2)
        # self.
        ####

        self.playlistView.activated.connect(self.jump)


        self.timeSlider.setRange(0, self.player.duration() / 1000)

        self.timeSlider.sliderMoved.connect(self.seek)
        # self.timeSlider.sliderPressed.connect(self.seek)

        # self.timeSlider.sliderPressed.connect(self.sliderPressed)
        #
        #self.slider.clicked.connect(self.seek)
        #

        self.playerState = QMediaPlayer.StoppedState
        self.playerMuted = False

        
        self.setState(self.player.state())
        self.setVolume(self.player.volume())
        self.setMuted(self.player.isMuted())
        

        # grab_btn=QtWidgets.QPushButton('Grab Screen')




        self.playButton.clicked.connect(self.playClicked)
        self.stopButton.clicked.connect(self.player.stop)
        self.nextButton.clicked.connect(self.playlist.next)
        self.previousButton.clicked.connect(self.playlist.previous)
        self.muteButton.clicked.connect(self.muteClicked)
        self.volumeSlider.sliderMoved.connect(self.player.setVolume)
        self.shuffleButton.clicked.connect(self.shufflelist)

        self.snapButton.clicked.connect(self.screenshot)
        
        self.actionColour_Options.triggered.connect(self.showColorDialog)
        # self.colorButton.clicked.connect(self.showColorDialog)

        self.actionOpen_Playlist.triggered.connect(self.trigger_open_playlist)
        self.actionSave_Playlist.triggered.connect(self.trigger_save_playlist)
        self.actionExit.triggered.connect(self.trigger_quit)
        self.actionDownload_Using_URL.triggered.connect(self.openDownloader)
        self.actionOpen_Browser.triggered.connect(self.openBrowser)
        self.actionOpen_Notemaker.triggered.connect(self.openWord)
        # displaySongInfo
        # self.actionColour_Options.triggered.connect(self.showColorDialog


        # QtCore.QObject.connect(self.actionSave_Playlist, QtCore.SIGNAL('triggered()'), self.trigger_save_playlist)
        # QtCore.QObject.connect(self.actionOpen_Playlist, QtCore.SIGNAL('triggered()'), self.trigger_open_playlist)

        # self.actionMy_playlist.triggered.connect(self.show_hide_playlist)
        # self.actionMy_playlist.setText('Hide my playlist')
        # self.dockWidget.visibilityChanged.connect(self.change_show_hide_menu_text)


        self.rateBox.activated.connect(self.updateRate)
        self.rateBox.addItem("0.5x", 0.5)
        self.rateBox.addItem("1.0x", 1.0)
        self.rateBox.addItem("2.0x", 2.0)
        self.rateBox.setCurrentIndex(1)

        self.playbackBox.activated.connect(self.changePlayback)
        self.playbackBox.addItem("Normal")
        self.playbackBox.addItem("Loop")
        self.playbackBox.addItem("Current Item Once")
        self.playbackBox.addItem("Current Item In Loop")
        self.playbackBox.addItem("Random")
        self.playbackBox.setCurrentIndex(0)
        # self.combo.activated.connect(self.handleActivated)


        # controls.changeRate.connect(self.player.setPlaybackRate)
        # self.playButton.clicked.connect(self.playClicked)
        # self.playButton.clicked.connect(self.playClicked)

        

        self.changeMuting.connect(self.player.setMuted)

        self.changeRate.connect(self.player.setPlaybackRate)

        self.player.stateChanged.connect(self.setState)
        self.player.volumeChanged.connect(self.setVolume)
        self.player.mutedChanged.connect(self.setMuted)
        # self.rateBox.activated.connect(self.setPlaybackRate)


        self.actionLoad.triggered.connect(self.open)

        self.setAcceptDrops(True)

        self.show()

    def mousePressEvent(self, QMouseEvent):
        # if QMouseEvent.button() == Qt.LeftButton:
        #     print("Left Button Clicked")
        if QMouseEvent.button() == Qt.RightButton:
            # do what you want here
            print("Right Button Clicked")




    def displaySongInfo(self):
        metaDataKeyList = self.player.availableMetaData()
        fullText = '<table class="tftable" border="0">'
        for key in metaDataKeyList:
            value = self.player.metaData(key)
            fullText = fullText + '<tr><td>' + key + '</td><td>' + str(value) + '</td></tr>'
        fullText = fullText + '</table>'
        infoBox = QMessageBox(self)
        infoBox.setWindowTitle('Detailed Song Information')
        infoBox.setTextFormat(Qt.RichText)
        infoBox.setText(fullText)
        infoBox.addButton('OK', QMessageBox.AcceptRole)
        infoBox.show()

    def openDownloader(self):
        self.MainApp = MainApp()
        self.MainApp.show()

    def openBrowser(self):
        self.Browser = Browser()
        self.Browser.show()



    def openWord(self):
        self.ProcessorWindow = ProcessorWindow()
        self.ProcessorWindow.show()

    def changePlayback(self,index):
    #     # self.changeRate.emit(self.playbackRate())    
    #     currentindex = self.rateBox.currentIndex()
        print(index)


        if index == 0:
            self.playlist.setPlaybackMode(QMediaPlaylist.Sequential)
            # self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
        elif index == 1:
            self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
            # self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemOnce)
        elif index == 2:
            # self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
            self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemOnce)
        elif index == 3:
            # self.playlist.setPlaybackMode(QMediaPlaylist.Random)
            self.playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)        
        else:
            self.playlist.setPlaybackMode(QMediaPlaylist.Random)        
    # def sliderPressed(self, t=-1):
    #     self.player.sliderPressed(self.player.positionvalue)   


    # def onRightClick(self):
    #     self.right = True


    # def on_playlistView_clicked(self, index):
    #     self.right = True
    #     # Show the context menu.
    #     self.menu.exec_(self.view.mapToGlobal(point))                  
         



    def screenshot(self):
        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(self.video.winId() )
        screenshot.save('shot.jpg', 'jpg')                           # needs adjustment/alteration
        # w.close()


    # def rotateVideo(self, angle):
       # x = self.videoItem.boundingRect().width() / 2.0
       # y = self.videoItem.boundingRect().height() / 2.0

       # self.videoItem.setTransform(
                #QTransform().translate(x, y).rotate(angle).translate(-x, -y))
    

    
    def state(self):
        return self.playerState

    def setState(self,state):

        icon_1 = QIcon()
        icon_1.addPixmap(QPixmap("images/control-pause.png"))
        icon_2 = QIcon()
        icon_2.addPixmap(QPixmap("images/control.png"))


        if state != self.playerState:               # m_playerState - self.playerState
            self.playerState = state

            if state == QMediaPlayer.StoppedState:              # switch-case  -   if-else
                self.stopButton.setEnabled(False)
                self.playButton.setIcon(icon_2)
            elif state == QMediaPlayer.PlayingState:
                self.stopButton.setEnabled(True)
                self.playButton.setIcon(icon_1)
            elif state == QMediaPlayer.PausedState:
                self.stopButton.setEnabled(True)
                self.playButton.setIcon(icon_2)

        


    #     if self.player.state() == QMediaPlayer.PlayingState:
    #         self.player.pause
    #         self.playButton.setIcon(icon_2)
    #         # self.toolButton_play_pause.setToolTip('Play')
    #         self.playButton.setToolTip('Play')
    #         # controls.setState(self.player.state())

    #     elif self.player.state() == QMediaPlayer.PausedState or self.player.state() == QMediaPlayer.StoppedState:
    #         self.player.play
    #         # controls.setState(self.player.state())
    #         self.playButton.setIcon(icon_1)
    #         self.playButton.setToolTip('Pause')

    def playbackRate(self):
        return self.rateBox.itemData(self.rateBox.currentIndex())

    def setPlaybackRate(self, rate):
        for i in range(self.rateBox.count()):
            if qFuzzyCompare(rate, self.rateBox.itemData(i)):
                self.rateBox.setCurrentIndex(i)
                return

        self.rateBox.addItem("%dx" % rate, rate)
        self.rateBox.setCurrentIndex(self.rateBox.count() - 1)

    def updateRate(self):
        self.changeRate.emit(self.playbackRate())




    def volume(self):
        return self.volumeSlider.value()

    def setVolume(self, volume):
        self.volumeSlider.setValue(volume)

    def isMuted(self):
        return self.playerMuted

    def setMuted(self, muted):
        if muted != self.playerMuted:
            self.playerMuted = muted

            self.muteButton.setIcon(
                    self.style().standardIcon(
                            QStyle.SP_MediaVolumeMuted if muted else QStyle.SP_MediaVolume))

    def playClicked(self):
        if self.playerState in (QMediaPlayer.StoppedState, QMediaPlayer.PausedState):
            self.player.play()
        elif self.playerState == QMediaPlayer.PlayingState:
            self.player.pause()



    def muteClicked(self):
        self.changeMuting.emit(not self.playerMuted)


    #: Open a previously saved playlist
    def trigger_open_playlist(self):
        # # Create a file dialog to load the playlist.
    
        filename, _ = QFileDialog.getOpenFileName(self,"Load play list", '', "Playlist (*.m3u);; All file (*.*)")
        # print(filename)
        try:
            self.playlist.load(QUrl.fromLocalFile(filename),".m3u") 
            print("The play list has been opened.")
            # int count = self.playlist.mediaCount();
            # for files in self.playlist.mediaCount():
            # QString test = self.playlist.media(count).canonicalUrl().fileName();
                # self.playlist.addMedia(QMediaContent(files))
        except:
            QMessageBox.warning(self, "Sorry, the play list cannot be opened!")    


        

    #: Save the current playlist
    def trigger_save_playlist(self):
        #: If playlist is empty do nothing
        
        if self.playlist is None or self.playlist.isEmpty():
            QMessageBox.about(self, "Warning", "There is nothing to save!")
        else:
            # Create a dialog showing the place to save the playlist.
            # QString = "Save play list"
            path, _ = QFileDialog.getSaveFileName(self,"Save play list", '', "Playlist (*.m3u);; All file (*.*)")
            # filename = str(filename.__str__())
            # print(path)
            # print(QUrl.fromLocalFile(path))
            try:
                # save the playlist.
                self.playlist.save(QUrl.fromLocalFile(path),"m3u") 
                print("The play list is saved.")
            except:
                QMessageBox.warning(self, "Sorry, the play list cannot be saved!")        



    #: Triggers the program to quit
    def trigger_quit(self):

        if QMessageBox.warning(None, 'Confirm', "Are you sure you want to quit?",
                            QMessageBox.Yes | QMessageBox.No,
                            QMessageBox.No) == QMessageBox.Yes:
            QApplication.quit()
    

    def shufflelist(self):
        self.playlist.shuffle()       
    



    # def change_show_hide_menu_text(self):
    #     """If the user manually closes the dock widget then it changes the show/hide playlist text
    #     in the view menu"""

    #     if self.dockWidget.isVisible() == True:
    #         self.actionMy_playlist.setText('Hide my playlist')
    #     else:
    #         self.actionMy_playlist.setText('Show my playlist')
    


    def showColorDialog(self):
        if self.colorDialog is None:
            brightnessSlider = QSlider(Qt.Horizontal)
            brightnessSlider.setRange(-100, 100)
            brightnessSlider.setValue(self.video.brightness())
            brightnessSlider.sliderMoved.connect(
                    self.video.setBrightness)
            self.video.brightnessChanged.connect(
                    brightnessSlider.setValue)

            contrastSlider = QSlider(Qt.Horizontal)
            contrastSlider.setRange(-100, 100)
            contrastSlider.setValue(self.video.contrast())
            contrastSlider.sliderMoved.connect(self.video.setContrast)
            self.video.contrastChanged.connect(contrastSlider.setValue)

            hueSlider = QSlider(Qt.Horizontal)
            hueSlider.setRange(-100, 100)
            hueSlider.setValue(self.video.hue())
            hueSlider.sliderMoved.connect(self.video.setHue)
            self.video.hueChanged.connect(hueSlider.setValue)

            saturationSlider = QSlider(Qt.Horizontal)
            saturationSlider.setRange(-100, 100)
            saturationSlider.setValue(self.video.saturation())
            saturationSlider.sliderMoved.connect(
                    self.video.setSaturation)
            self.video.saturationChanged.connect(
                    saturationSlider.setValue)

            layout = QFormLayout()
            layout.addRow("Brightness", brightnessSlider)
            layout.addRow("Contrast", contrastSlider)
            layout.addRow("Hue", hueSlider)
            layout.addRow("Saturation", saturationSlider)

            button = QPushButton("Close")
            layout.addRow(button)

            self.colorDialog = QDialog(self)
            self.colorDialog.setWindowTitle("Color Options")
            self.colorDialog.setLayout(layout)

            button.clicked.connect(self.colorDialog.close)

        self.colorDialog.show()
            
        




        if not self.player.isAvailable():
            QMessageBox.warning(self, "Service not available",
                    "The QMediaPlayer object does not have a valid service.\n"
                    "Please check the media service plugins are installed.")

            # controls.setEnabled(False)
            self.playlistView.setEnabled(False)
            # openButton.setEnabled(False)
            # self.colorButton.setEnabled(False)
            self.fullscreenButton.setEnabled(False)

        # self.metaDataChanged()

        # self.addToPlaylist(playlist)

    def open(self):
        fileNames, _ = QFileDialog.getOpenFileNames(self, "Open Files")

        if fileNames == []:
            # If no media files have been selected then don't execute the rest of the code.
            return

        self.addToPlaylist(fileNames)

    def addToPlaylist(self, fileNames):
        for name in fileNames:
            fileInfo = QFileInfo(name)
            # print(fileInfo)
            if fileInfo.exists():
                url = QUrl.fromLocalFile(fileInfo.absoluteFilePath())
                # print(url)
                if fileInfo.suffix().lower() == 'm3u':
                    self.playlist.load(url)
                else:
                    self.playlist.addMedia(QMediaContent(url))
            else:
                url = QUrl(name)
                # print(url)
                if url.isValid():
                    self.playlist.addMedia(QMediaContent(url))
                    # print(QMediaContent(url))

    def durationChanged(self, duration):
        duration /= 1000

        self.duration = duration
        self.timeSlider.setMaximum(duration)

    def positionChanged(self, progress):
        progress /= 1000

        if not self.timeSlider.isSliderDown():
            self.timeSlider.setValue(progress)

        self.updateDurationInfo(progress)

    # def metaDataChanged(self):
    #     if self.player.isMetaDataAvailable():
    #         self.setTrackInfo("%s - %s" % (
    #                 self.player.metaData(QMediaMetaData.AlbumArtist),
    #                 self.player.metaData(QMediaMetaData.Title)))

    def previousClicked(self):
        # Go to the previous track if we are within the first 5 seconds of
        # playback.  Otherwise, seek to the beginning.
        if self.player.position() <= 5000:
            self.playlist.previous()
        else:
            self.player.setPosition(0)

    def jump(self, index):
        if index.isValid():
            self.playlist.setCurrentIndex(index.row())
            self.player.play()

    def playlistPositionChanged(self, position):
        self.playlistView.setCurrentIndex(
                self.playlistModel.index(position, 0))

    def seek(self, seconds):
        self.player.setPosition(seconds * 1000)

    def statusChanged(self, status):
        self.handleCursor(status)

        if status == QMediaPlayer.LoadingMedia:
            self.setStatusInfo("Loading...")
        elif status == QMediaPlayer.StalledMedia:
            self.setStatusInfo("Media Stalled")
        elif status == QMediaPlayer.EndOfMedia:
            QApplication.alert(self)
        elif status == QMediaPlayer.InvalidMedia:
            self.displayErrorMessage()
        else:
            self.setStatusInfo("")

    def handleCursor(self, status):
        if status in (QMediaPlayer.LoadingMedia, QMediaPlayer.BufferingMedia, QMediaPlayer.StalledMedia):
            self.setCursor(Qt.BusyCursor)
        else:
            self.unsetCursor()

    def bufferingProgress(self, progress):
        self.setStatusInfo("Buffering %d%" % progress)

    def videoAvailableChanged(self, available):
        if available:
            self.fullscreenButton.clicked.connect(
                    self.video.setFullScreen)
            self.video.fullScreenChanged.connect(
                    self.fullscreenButton.setChecked)

            if self.fullscreenButton.isChecked():
                self.video.setFullScreen(True)
        else:
            # self.fullscreenButton.clicked.disconnect(self.video.setFullScreen)
            # self.video.fullScreenChanged.disconnect(self.fullscreenButton.setChecked)

            self.video.setFullScreen(False)

        # self.colorButton.setEnabled(available)

    def setTrackInfo(self, info):
        self.trackInfo = info

        if self.statusInfo != "":
            self.setWindowTitle("%s | %s" % (self.trackInfo, self.statusInfo))          # %1 | %2 - %s | %s
        else:
            self.setWindowTitle(self.trackInfo)

    def setStatusInfo(self, info):
        self.statusInfo = info

        if self.statusInfo != "":
            self.setWindowTitle("%s | %s" % (self.trackInfo, self.statusInfo))
        else:
            self.setWindowTitle(self.trackInfo)

    def displayErrorMessage(self):
        self.setStatusInfo(self.player.errorString())

    def updateDurationInfo(self, currentInfo):
        duration = self.duration
        if currentInfo or duration:
            currentTime = QTime((currentInfo/3600)%60, (currentInfo/60)%60,
                    currentInfo%60, (currentInfo*1000)%1000)
            totalTime = QTime((duration/3600)%60, (duration/60)%60,
                    duration%60, (duration*1000)%1000);

            format = 'hh:mm:ss' if duration > 3600 else 'mm:ss'
            tStr = currentTime.toString(format) + " / " + totalTime.toString(format)
        else:
            tStr = ""

        self.track_time.setText(tStr)

    



#}########################################################################################################

        


    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            self.playlist.addMedia(
                QMediaContent(url)
            )

        self.playlistModel.layoutChanged.emit()


    def erroralert(self, *args):
        print(args)

    

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("PSVM")
    app.setStyle("Fusion")

    # Fusion dark palette from https://gist.github.com/QuantumCD/6245215.
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

    window = MainWindow()
    app.exec_()
