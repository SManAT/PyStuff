#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Stefan Hagmann

import time
from pathlib import Path
from PyQt5.Qt import QPixmap, QProgressBar, Qt, QDialog
from PyQt5.QtWidgets import QSplashScreen
from PyQt5 import QtGui, QtCore, uic, QtWidgets
from threading import Thread


class SplashScreen_Core(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 100, 50))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "UI_Dialog"))
        self.pushButton.setText(_translate("Dialog", "OK"))


class SplashScreen(QtWidgets.QDialog):
    """ Display a Splashscreen """
    signal_show = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(SplashScreen, self).__init__(parent)

        self.rootDir = Path(__file__).parent
        uifile = self.rootDir.joinpath('splash.ui')
        self.ui = uic.loadUi(uifile)        # load UI


        #image = self.rootDir.joinpath("img/loading.jpg").as_posix()

    # Splashscreen ===============================================================
    def show_splash(self):
        """ show the splashscreen in Thread """
        t = Thread(target=self.show_splash_dialog)
        t.daemon = True
        t.start()
        
    def complete_dialog(self):
        self.splash_done = True

    def wait_for_splash(self):
        while not self.splash_done:
            #self.progress += 1
            #if(self.progress>100):
            #    self.progress = 0
            #self.updateProgressBar()
            time.sleep(0.1)

        self.splash_done = False


    def show_splash_dialog(self):
        super(SplashScreen, self).exec_()
        self.signal_show.emit()

        # Wait for the dialog to get closed
        self.wait_for_splash()
 
        
