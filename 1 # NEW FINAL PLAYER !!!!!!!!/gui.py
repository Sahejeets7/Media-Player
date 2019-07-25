# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 642)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/gui-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.video = QVideoWidget(self.centralwidget)
        self.video.setMinimumSize(QtCore.QSize(0, 500))
        self.video.setAutoFillBackground(False)
        self.video.setObjectName("video")
        self.verticalLayout.addWidget(self.video)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.timeSlider = QtWidgets.QSlider(self.centralwidget)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.horizontalLayout_3.addWidget(self.timeSlider)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.track_time = QtWidgets.QLabel(self.centralwidget)
        self.track_time.setObjectName("track_time")
        self.horizontalLayout_2.addWidget(self.track_time)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previousButton = QtWidgets.QToolButton(self.centralwidget)
        self.previousButton.setStyleSheet("QToolButton{\n"
"border: none ;\n"
"background: transparent ;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color : rgb(203, 203, 203)\n"
"}\n"
"\n"
"")
        self.previousButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/control-skip-180.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousButton.setIcon(icon1)
        self.previousButton.setIconSize(QtCore.QSize(40, 40))
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout.addWidget(self.previousButton)
        self.playButton = QtWidgets.QToolButton(self.centralwidget)
        self.playButton.setStyleSheet("QToolButton{\n"
"border: none ;\n"
"background: transparent ;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color : rgb(203, 203, 203)\n"
"}\n"
"\n"
"")
        self.playButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/control.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon2)
        self.playButton.setIconSize(QtCore.QSize(40, 40))
        self.playButton.setObjectName("playButton")
        self.horizontalLayout.addWidget(self.playButton)
        self.nextButton = QtWidgets.QToolButton(self.centralwidget)
        self.nextButton.setStyleSheet("QToolButton{\n"
"border: none ;\n"
"background: transparent ;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color : rgb(203, 203, 203)\n"
"}\n"
"\n"
"")
        self.nextButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/control-skip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon3)
        self.nextButton.setIconSize(QtCore.QSize(40, 40))
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout.addWidget(self.nextButton)
        self.stopButton = QtWidgets.QToolButton(self.centralwidget)
        self.stopButton.setStyleSheet("QToolButton{\n"
"border: none ;\n"
"background: transparent ;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color : rgb(203, 203, 203)\n"
"}\n"
"\n"
"")
        self.stopButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/control-stop-square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon4)
        self.stopButton.setIconSize(QtCore.QSize(40, 40))
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        self.shuffleButton = QtWidgets.QToolButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/shuffle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shuffleButton.setIcon(icon5)
        self.shuffleButton.setIconSize(QtCore.QSize(20, 20))
        self.shuffleButton.setObjectName("shuffleButton")
        self.horizontalLayout.addWidget(self.shuffleButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.rateBox = QtWidgets.QComboBox(self.centralwidget)
        self.rateBox.setObjectName("rateBox")
        self.horizontalLayout.addWidget(self.rateBox)
        self.muteButton = QtWidgets.QToolButton(self.centralwidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/speaker-volume.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.muteButton.setIcon(icon6)
        self.muteButton.setObjectName("muteButton")
        self.horizontalLayout.addWidget(self.muteButton)
        self.volumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout.addWidget(self.volumeSlider)
        self.fullscreenButton = QtWidgets.QToolButton(self.centralwidget)
        self.fullscreenButton.setStyleSheet("QToolButton{\n"
"border: none ;\n"
"background: transparent ;\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"background-color : rgb(203, 203, 203)\n"
"}\n"
"\n"
"")
        self.fullscreenButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/full-screen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fullscreenButton.setIcon(icon7)
        self.fullscreenButton.setIconSize(QtCore.QSize(35, 35))
        self.fullscreenButton.setObjectName("fullscreenButton")
        self.horizontalLayout.addWidget(self.fullscreenButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.playlistView = QtWidgets.QListView(self.dockWidgetContents)
        self.playlistView.setStyleSheet("QPushButton{\n"
"background : trasperent\n"
"}\n"
"")
        self.playlistView.setObjectName("playlistView")
        self.verticalLayout_2.addWidget(self.playlistView)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionOpen_Playlist = QtWidgets.QAction(MainWindow)
        self.actionOpen_Playlist.setObjectName("actionOpen_Playlist")
        self.actionMy_playlist = QtWidgets.QAction(MainWindow)
        self.actionMy_playlist.setObjectName("actionMy_playlist")
        self.actionColour_Options = QtWidgets.QAction(MainWindow)
        self.actionColour_Options.setObjectName("actionColour_Options")
        self.actionSave_Playlist = QtWidgets.QAction(MainWindow)
        self.actionSave_Playlist.setObjectName("actionSave_Playlist")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionOpen_Playlist)
        self.menuFile.addAction(self.actionSave_Playlist)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionMy_playlist)
        self.menuView.addAction(self.actionColour_Options)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyPlayer"))
        self.track_time.setToolTip(_translate("MainWindow", "Current time | Total time"))
        self.track_time.setText(_translate("MainWindow", "00:00 | 00:00"))
        self.previousButton.setToolTip(_translate("MainWindow", "Previous track"))
        self.playButton.setToolTip(_translate("MainWindow", "Play or Pause"))
        self.nextButton.setToolTip(_translate("MainWindow", "Next track"))
        self.stopButton.setToolTip(_translate("MainWindow", "Stop"))
        self.shuffleButton.setText(_translate("MainWindow", "..."))
        self.muteButton.setText(_translate("MainWindow", "..."))
        self.fullscreenButton.setToolTip(_translate("MainWindow", "Fullscreen (Press Esc key to exit)"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "My playlist"))
        self.playlistView.setToolTip(_translate("MainWindow", "Playlist"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionOpen_Playlist.setText(_translate("MainWindow", "Open Playlist"))
        self.actionMy_playlist.setText(_translate("MainWindow", "My_playlist"))
        self.actionColour_Options.setText(_translate("MainWindow", "Colour Options..."))
        self.actionSave_Playlist.setText(_translate("MainWindow", "Save Playlist"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

from PyQt5.QtMultimediaWidgets import QVideoWidget
