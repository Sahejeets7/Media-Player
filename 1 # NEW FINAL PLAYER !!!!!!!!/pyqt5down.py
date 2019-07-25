##PyQt4
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *
# from PyQt4.uic import loadUIType


##PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

import urllib
import pafy
import humanize

import os
from os import path
import sys

# import UI File to use it in the next class that runs the GUI in pycharm
# when you make change in Qt designer it change automatic here
FORM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "d2.ui"))

# Initiate UI File
class MainApp(QMainWindow, FORM_CLASS):

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI()
        self.Handle_Buttons()


    def Handle_UI(self):
        self.setWindowTitle('Downloader')
        self.setFixedSize(707,397)

    def Handle_Buttons(self):
        self.downloadButton1.clicked.connect(self.Download)
        self.browseButton1.clicked.connect(self.Handle_Browse)
        self.searchButton.clicked.connect(self.Get_Youtube_Video)
        self.downloadButton2.clicked.connect(self.Download_Youtube_Video)
        self.browseButton2.clicked.connect(self.Save_Browse)
        self.browseButton3.clicked.connect(self.Save_Browse)
        self.downloadButton3.clicked.connect(self.Playlist_Download)


    def Handle_Browse(self):
        save_place = QFileDialog.getSaveFileName(self, caption="Save As", directory = ".", filter="All Files (*.*)")
        text = str(save_place)
        name = (text[2:].split(',')[0].replace("'", ""))
        self.location1.setText(name)                           # for downloading file!


    def Progress(self, blocknum, blocksize, totalsize):
        # this is how progress bar act it needs these three arguments
        read = blocknum * blocksize

        # display the progress:
        if totalsize > 0:
            percent = read * 100 / totalsize
            self.progressBar1.setValue(percent)
            QApplication.processEvents()  # To Prevent Not Responding

        # display downloaded size:
        # downloaded_mb = humanize.naturalsize(read)
        # self.textBrowser_4.setText(downloaded_mb)


    def Save_Browse(self):
        save = QFileDialog.getExistingDirectory(self, "select Download Directory")
        self.location2.setText(save)                                             # for downloading video!
        self.location3.setText(save)


    def Download(self):
        # url & location
        url = self.url1.text()
        save_location = self.location1.text()
        try:
            urllib.request.urlretrieve(url, save_location, self.Progress)              # download file
        except Exception:
            QMessageBox.warning(self, "Download Error", "The Download Failed")
            return

        QMessageBox.information(self, "Download Completed", "The Downlodad Finished")
        self.progressBar1.setValue(0)
        self.url1.setText('')
        self.location1.setText('')



    def Get_Youtube_Video(self):
        video_link = self.url2.text()
        v = pafy.new(video_link)
        # print(v.title)
        # print(v.duration)
        # print(v.rating)
        # print(v.author)
        # print(v.length)
        # print(v.keywords)
        # print(v.thumb)
        # print(v.videoid)
        # print(v.viewcount)
        st = v.allstreams

        for s in st:
            size = humanize.naturalsize(s.get_filesize())
            data = '{} {} {} {}'.format(s.mediatype, s.extension, s.quality, size)
            self.qualitycomboBox1.addItem(data)

        QApplication.processEvents()

    def Download_Youtube_Video(self):
        video_link = self.url2.text()
        save_location = self.location2.text()
        v = pafy.new(video_link)
        st = v.videostreams
        quality = self.qualitycomboBox1.currentIndex()   # to know which item is selected!

        down = st[quality].download(filepath=save_location)
        QMessageBox.information(self, "Download Completed", "The Video has finished Downloading!!")
        QApplication.processEvents()

    def Playlist_Download(self):
        playlist_url = self.url3.text()
        save_location = self.location3.text()
        QApplication.processEvents()
        playlist = pafy.get_playlist(playlist_url)
        videos = playlist['items']

        os.chdir(save_location)
        os.mkdir(str(playlist['title']))
        os.chdir(str(playlist['title']))

        for video in videos:
            p = video['pafy']
            best = p.getbest(preftype = 'mp4')
            best.download()
        QApplication.processEvents()

    app = QApplication(sys.argv)
def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    # palette = QPalette()
    # palette.setColor(QPalette.ButtonText, Qt.red)
    # app.setPalette(palette)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
