#!/usr/bin/env python3
import sys
import threading
import time
from pathlib import Path
import PyQt5
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication
import random


class MAIN_UI(PyQt5.QtWidgets.QMainWindow):
    startNotification_Signal = pyqtSignal(Notification)
    endNotification_Signal = pyqtSignal(Notification)

    def __init__(self, parent=None):
        super(MAIN_UI, self).__init__(parent)
        self.rootDir = Path(__file__).parent
        uifile = self.rootDir.joinpath('main.ui')
        self.ui = uic.loadUi(uifile)        # load UI
        self.ui.btn1.clicked.connect(lambda: self.startNotificationTest())

        self.ui.show()

    def _showNotification(self, n):
        """ shows the notification n """
        n.show()

    def _hideNotification(self, n):
        """ hides the notification n """
        n.hide()

    def _showInformationNotification(self, msg):
        """ shows a Information Notification """
        notification = Notification()
        notification.setHeader("Information")
        notification.setMessage(msg)
        notification.setIcon('pixmaps/notice.png')

        x = random.randrange(100, 800)
        y = random.randrange(100, 800)
        notification.moveTo(x, y)

        self.startNotification_Signal.connect(self.showNotification)
        self.endNotification_Signal.connect(self.hideNotification)

        self.startNotification_Signal.emit(notification)
        time.sleep(notification.getTimeout())
        self.endNotification_Signal.emit(notification)

    def _showSuccessNotification(self, msg):
        """ shows a Information Notification """
        notification = Notification()
        notification.setHeader("Done")
        notification.setMessage(msg)
        notification.setIcon('pixmaps/success.png')

        x = random.randrange(100, 800)
        y = random.randrange(100, 800)
        notification.moveTo(x, y)

        self.startNotification_Signal.connect(self.showNotification)
        self.endNotification_Signal.connect(self.hideNotification)

        self.startNotification_Signal.emit(notification)
        time.sleep(notification.getTimeout())
        self.endNotification_Signal.emit(notification)

    def showInformation(self, msg):
        """ shows a notification within a thread """
        t = threading.Thread(target=self.showInformationNotification, args=[msg])
        t.daemon = True
        t.start()

    def showSuccess(self, msg):
        """ shows a notification within a thread """
        t = threading.Thread(target=self._showSuccessNotification, args=[msg])
        t.daemon = True
        t.start()

    def startNotificationTest(self):
        texte = ["Vor langer langer Zeit lebte ein Tux in Österreich und hatte keine Windows daheim",
                 "Quod erat demonsdrandum",
                 "Einer der nichts weiß und nicht weiß das er nichts weiß, weiß weniger als einer der weiß dass er nichts weiß"]
        for i in range(0, 3):
            print("%s %s" % (i, texte[i]))
            """ start showing Notification within a Thread for non blocking """
            self.showInformation(texte[i])


def main():
    app = QApplication(sys.argv)

    # show main Window
    mainUI = MAIN_UI()  #noqa

    app.exec_()


if __name__ == '__main__':
    main()
