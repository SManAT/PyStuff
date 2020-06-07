#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Stefan Hagmann

import time
from pathlib import Path
from PyQt5.Qt import QPixmap, QProgressBar, Qt, QDialog
from PyQt5.QtWidgets import QSplashScreen
from PyQt5 import QtGui, QtCore, uic, QtWidgets
from threading import Thread

class SplashScreen(QtWidgets.QDialog):
    """ Display a Splashscreen """
    signal_show = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(SplashScreen, self).__init__(parent)

        self.rootDir = Path(__file__).parent
        uifile = self.rootDir.joinpath('splash.ui')
        self.ui = uic.loadUi(uifile)        # load UI
        # this will hide the app from task bar
        self.ui.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.ui.setAttribute(QtCore.Qt.WA_ShowWithoutActivating)
        self.setModal(False)


        #image = self.rootDir.joinpath("img/loading.jpg").as_posix()

    def done(self):
        """ becomes called, when all is preloaded
        set flag for stopping the thread """
        self.close()
        print("done")

    def show_splash(self):
        """ show the splashscreen in Thread """
        t = Thread(target=self.show_splash_dialog)
        t.daemon = True
        t.setName("SplashThread")
        t.start()

    def show_splash_dialog(self):
        # display it
        self.ui.show()
        self.signal_show.emit()

        # Wait for the dialog to get closed
        while not self.splash_done:
            #self.progress += 1
            #if(self.progress>100):
            #    self.progress = 0
            #self.updateProgressBar()
            time.sleep(1)
            print("tick")
        print("Im done")
        self.splash_done = False
