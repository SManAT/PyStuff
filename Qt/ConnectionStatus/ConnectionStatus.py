#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Stefan Hagmann
from pathlib import Path
from PyQt5 import uic, QtWidgets, QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QGuiApplication
import time
import random
from enum import Enum
from PyQt5.Qt import QObject
import threading


class ConnectionStatus(QtWidgets.QDialog):
    """ Display a Status Window for some reasons """
    def __init__(self, parent=None):
        super(ConnectionStatus, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.rootDir = Path(__file__).parent
        uifile = self.rootDir.joinpath('status.ui')
        self.ui = uic.loadUi(uifile)        # load UI
        # this will hide the app from task bar
        self.ui.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.ui.setAttribute(QtCore.Qt.WA_ShowWithoutActivating)
        self.setModal(False)

        self.moveToDefaultPosition()


    def show(self):
        """ show it """
        # self.ticker.start()
        self.ui.show()

    def hide(self):
        """ show it """
        self.ui.hide()

    def _onAbbrechen(self):
        """ click event, hide it"""
        self.close()
        
    def setType(self, typ):
        if typ==1:
            self.setIcon("connected.png")
        else:
            self.setIcon("disconnected.png")

    def setMessage(self, txt):
        """ set the Message of the notification """
        self.ui.text.setText(txt)

    def setIcon(self, icon):
        iconfile = self.rootDir.joinpath("img/"+icon).as_posix()
        self.ui.icon.setPixmap(QPixmap(iconfile))

    def moveToDefaultPosition(self):
        """ the default position right bottom of screen """
        self.ui.adjustSize()
        # get main screen
        screen = QGuiApplication.screens()[0]
        taskbar_height = screen.geometry().height() - screen.availableVirtualGeometry().height()
        self.ui.move(screen.geometry().width(), screen.geometry().height() - taskbar_height)
        x = screen.geometry().width() - self.ui.width()
        y = screen.availableVirtualGeometry().height() - self.ui.height()
        self.ui.move(x, y)




    def showInformation(self, msg):
        self._notification.setType(Notification_Type.Information)
        self._notification.setMessage(msg)
        t = threading.Thread(target=self._createNotification)
        t.daemon = True
        t.start()
