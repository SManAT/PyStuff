#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Stefan Hagmann

import sys
import time
from pathlib import Path
import PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.Qt import QCoreApplication
from Qt.Splashscreen.SplashScreen import SplashScreen


class MAIN_UI(PyQt5.QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MAIN_UI, self).__init__(parent)
        self.rootDir = Path(__file__).parent
        uifile = self.rootDir.joinpath('main.ui')
        self.ui = uic.loadUi(uifile, self)        # load UI inside QMainWindow
        self.ui.close.clicked.connect(lambda: self.close())

    def close(self):
        QCoreApplication.quit()

    def closeEvent(self, event):
        ''' window tries to close '''
        # event.ignore()
        pass


def main():
    app = QApplication(sys.argv)

    splash = SplashScreen()

    for i in range(1, 101):
        splash.progressBar.setValue(i)
        t = time.time()
        while time.time() < t + 0.1:
            # mainthread must process Events
            app.processEvents()

    # Simulate something that takes time
    time.sleep(1)

    # show main Window
    gui = MAIN_UI()  #noqa
    gui.show()

    splash.finish(gui)
    app.exec_()


if __name__ == '__main__':
    main()
