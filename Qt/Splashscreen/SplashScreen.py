#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Stefan Hagmann

from pathlib import Path
from PyQt5.Qt import QProgressBar, QFont, QColor
from PyQt5.QtWidgets import QSplashScreen
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QGuiApplication
from Qt.OvelayIcons.OpenCVLib import OpenCVLib


class SplashScreen(QSplashScreen):
    """ Display a Splashscreen """

    signal_done = QtCore.pyqtSignal()

    def __init__(self):
        QSplashScreen.__init__(self, QtGui.QPixmap(), QtCore.Qt.WindowStaysOnTopHint)

        self.rootDir = Path(__file__).parent

        # default values
        self.image = self.rootDir.joinpath("img/loading.jpg").as_posix()
        self.version = "3.x"

        self.cv = OpenCVLib()

        self.progressBar = QProgressBar(self)
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)
        self.progressBar.setMaximum(100)
        # center on screen
        margin = 10
        # x, y, w, h
        self.progressBar.setGeometry(margin, self.pixmap().height() - 50,
                                     self.pixmap().width() - 2 * margin, 20)
        self.progressBar.setTextVisible(False)

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

    def scale(self, pix):
        gold = 0.618
        h = pix.height()

        # max width 68% of screen
        screen = QGuiApplication.screens()[0]
        new_w = screen.geometry().width() * gold
        new_h = h * gold
        # print("%s x %s" %(w, h))
        # python resize
        # return pix.scaled(new_w, new_h, Qt.KeepAspectRatioByExpanding | Qt.SmoothTransformation)
        # resize with opencv
        Qimg = pix.toImage()
        img = self.cv.QImage2MAT(Qimg)
        resized = self.cv.resizeTo(img, new_w, new_h)
        return self.cv.MAT2QPixmap(resized)

    def setVersion(self, version):
        """ adds a Version Number and updates the image """
        self.version = version
        self.setImage(self.image)

    def setImage(self, img):
        """ sets the image and adds a Version Number """
        self.image = self.image = self.rootDir.joinpath(img).as_posix()
        splash_pix = QtGui.QPixmap(img)
        # Add version
        painter = QtGui.QPainter()
        painter.begin(splash_pix)

        painter.setFont(QFont("Arial", 8, QFont.Bold))
        painter.setPen(QColor("#000000"))
        painter.drawText(0, 0, splash_pix.size().width() - 3,
                         splash_pix.size().height() - 1,
                         QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight, self.version)
        painter.end()
        self.setPixmap(self.scale(splash_pix))

    def _incProgressbar(self):
        self.progressBar.setValue(self.progressBar.value() + 1)

    def step(self):
        """ a preloading step is done """
        # check if maximum is reached
        self._incProgressbar()
        self.progressBar.repaint()

        if(self.progressBar.value() >= (self.progressBar.maximum() - 1)):
            self.signal_done.emit()

    def setProgressMax(self, maxval):
        self.progressBar.setMaximum(maxval)
