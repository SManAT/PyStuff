#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Stefan Hagmann

from pathlib import Path
from PyQt5.Qt import QPixmap, QProgressBar, Qt
from PyQt5.QtWidgets import QSplashScreen
from PyQt5 import QtGui, QtCore


class SplashScreen(QSplashScreen):
    """ Display a Splashscreen """

    def __init__(self, parent=None):
        super(SplashScreen, self).__init__(parent)

        self.rootDir = Path(__file__).parent
        image = self.rootDir.joinpath("img/loading.jpg").as_posix()
        
        self.version = "3.4"
        
        splash_pix = QtGui.QPixmap(image)
        ## Add version
        painter = QtGui.QPainter()
        painter.begin(splash_pix)
        painter.setPen(QtCore.Qt.white)
        painter.drawText(0, 0, splash_pix.size().width()-3, splash_pix.size().height()-1, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight, self.version)
        painter.end()
        

        self.setPixmap(QPixmap(image))
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setEnabled(False)

        self.progressBar = QProgressBar(self)
        self.progressBar.setMaximum(100)
        # center on screen
        self.progressBar.setGeometry(0, self.pixmap().height() - 50, self.pixmap().width(), 20)
        self.progressBar.setTextVisible(False)
        
        self.progressBar.resize(self.width(), 20)
        
        # CSS Styling
        self.setStyleSheet("""
            QProgressBar:horizontal {
                border: 1px solid gray;
                background: white;
                padding: 0;
                text-align: right;
                margin-top: 10px;
            }
            """)
        
        self.splashMsg.setStyleSheet("font-weight:bold;color:purple")
        self.splash.setMask(splash_pix.mask())


        self.show()
        self.showMessage("<h1><font color='green'>Welcome BeeMan!</font></h1>", Qt.AlignTop | Qt.AlignCenter, Qt.black)
        

    