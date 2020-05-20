#!/usr/bin/env python3
from pathlib import Path
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap


class Notification(QtWidgets.QDialog):
    """ Display a Notification for some reasons """
    def __init__(self, parent=None):
        super(Notification, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.rootDir = Path(__file__).parent
        uifile = self.rootDir.joinpath('Notification.ui')
        self.ui = uic.loadUi(uifile)        # load UI
        self.ui.setWindowFlags(Qt.FramelessWindowHint)

        self.ui.adjustSize()
        # position right middle of screen
        screen = QApplication.instance().desktop().screen().rect()
        self.ui.move(screen.width() - self.ui.width(), (screen.height() - self.ui.height()) // 2)
        iconfile = self.rootDir.joinpath('pixmaps/success.png').as_posix()
        self.ui.icon.setPixmap(QPixmap(iconfile))

        self.ui.exit.clicked.connect(self._onAbbrechen)
        self._timeout = 4  # sec

    def moveTo(self, x, y):
        """ move the dialog on the screen """
        self.ui.move(x, y)

    def show(self):
        """ show it """
        # self.ticker.start()
        self.ui.show()

    def hide(self):
        """ show it """
        self.ui.hide()

    def _onAbbrechen(self):
        """ click event, hide it"""
        self.hide()

    def setHeader(self, txt):
        """ set the Header of the notification """
        self.ui.header.setText(txt)

    def setMessage(self, txt):
        """ set the Message of the notification """
        self.ui.text.setText(txt)

    def setTimeout(self, time):
        """ how long should the notification be displayed in sec """
        self._timeout = time

    def getTimeout(self):
        return self._timeout

    def setIcon(self, icon):
        iconfile = self.rootDir.joinpath(icon).as_posix()
        self.ui.icon.setPixmap(QPixmap(iconfile))
