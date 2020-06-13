#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Stefan Hagmann

from pathlib import Path
from PyQt5.Qt import QProgressBar, QFont, QColor, Qt
from PyQt5.QtWidgets import QSplashScreen, QLabel
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
        # pixmap.height - ?
        self.progress_y = 60
        # Version Font Size
        self.vsize = 24
        # pixmap.width - ?
        self.vx = 16
        # pixmap.height - ?
        self.vy = 26
        # message font size
        self.msize = 12

        self.cv = OpenCVLib()

        self.progressBar = QProgressBar(self)
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setTextVisible(False)
        self.setPositionProgressBar()

        self.message = QLabel(self)
        self.message.setFont(QFont("Arial", self.msize, QFont.Bold))
        self.message.setStyleSheet("QLabel { color : #FFFFFF; }")
        self.message.setAlignment(Qt.AlignCenter)
        self.setPositionMessage()
        # self.message.hide()

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

    def setMessage(self, msg):
        self.message.setText("%s ..." % (msg))
        self.message.show()

    def setPositionMessage(self):
        """ place Message on screen """
        # where is progress?
        p = self.progressBar.geometry()
        self.message.setGeometry(0, p.y() - self.msize,
                                 self.pixmap().width(), 2 * self.msize)
        self.message.updateGeometry()

    def setPositionProgressBar(self):
        """ place ProgressBar on screen """
        margin = 10
        # x, y, w, h
        self.progressBar.setGeometry(margin, self.pixmap().height() - self.progress_y,
                                     self.pixmap().width() - 2 * margin, 20)
        self.progressBar.updateGeometry()

    def scale(self, pix):
        gold = 0.618
        h = pix.height()
        w = pix.width()

        # max width 68% of screen
        screen = QGuiApplication.screens()[0]
        new_w = screen.geometry().width() * gold
        new_h = h * new_w / w
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
        self.image = self.rootDir.joinpath(img).as_posix()
        splash_pix = QtGui.QPixmap(img)
        # Add version
        painter = QtGui.QPainter()
        painter.begin(splash_pix)

        painter.setFont(QFont("Arial", self.vsize, QFont.Bold))
        painter.setPen(QColor("#FFFFFF"))
        painter.drawText(0, 0, splash_pix.size().width() - self.vx,
                         splash_pix.size().height() - self.vy,
                         QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight, self.version)
        painter.end()
        self.setPixmap(self.scale(splash_pix))
        # ----------------------------------------------
        # other stuff
        self.setPositionProgressBar()
        self.setPositionMessage()

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
