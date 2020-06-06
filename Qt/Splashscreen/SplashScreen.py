#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Stefan Hagmann

from pathlib import Path
from PyQt5.Qt import QPixmap, QProgressBar, Qt
from PyQt5.QtWidgets import QSplashScreen


class SplashScreen(QSplashScreen):
    """ Display a Splashscreen """

    def __init__(self, parent=None):
        super(SplashScreen, self).__init__(parent)

        self.splash_pix = QPixmap('img/loading.jpg')

        splash = QSplashScreen(self.splash_pix, Qt.WindowStaysOnTopHint)
        splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        splash.setEnabled(False)

        self.progressBar = QProgressBar(self)
        self.progressBar.setMaximum(10)
        self.progressBar.setGeometry(0, self.splash_pix.height() - 50, self.splash_pix.width(), 20)
        self.show()
        self.showMessage("<h1><font color='green'>Welcome BeeMan!</font></h1>", Qt.AlignTop | Qt.AlignCenter, Qt.black)

    