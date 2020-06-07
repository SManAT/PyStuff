#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Stefan Hagmann

import sys
import time
from pathlib import Path
import PyQt5
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.Qt import QCoreApplication
from Qt.Splashscreen.SplashScreen import SplashScreen
from threading import Thread
from multiprocessing import Pool


class MAIN_UI(PyQt5.QtWidgets.QMainWindow):
    # fire if preloading is done
    loading_done_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MAIN_UI, self).__init__(parent)
        self.rootDir = Path(__file__).parent
        uifile = self.rootDir.joinpath('main.ui')
        self.ui = uic.loadUi(uifile, self)        # load UI inside QMainWindow
        self.ui.close.clicked.connect(lambda: self.close())

    def updateProgressBar(self):
        self.ui.progressBar.setValue(self.progress)

    def close(self):
        QCoreApplication.quit()

    def closeEvent(self, event):
        ''' window tries to close '''
        # event.ignore()
        pass

def preload():
    """ here we are loading all data that we need """
    time.sleep(2)
    return 0


def main():
    app = QApplication(sys.argv)
    """
    splash = SplashScreen()
    splash.show_splash()
    # create MAin Window, takes some time
    gui = MAIN_UI(splash)  #noqa
    gui.preload()
    splash.close()
    """  
       
    
    # Create and display the splash screen
    splash = SplashScreen()
#   splash.setMask(splash_pix.mask())
    #splash.raise_()
    splash.show()
    app.processEvents()
    # this event loop is needed for dispatching of Qt events
    initLoop = QtCore.QEventLoop()
    pool = Pool(processes=1)
    pool.apply_async(preload, None, callback=lambda exitCode: initLoop.exit(exitCode))
    initLoop.exec_()
    
    gui = MAIN_UI()  #noqa
    gui.preload()

    
    
    
    
    
    gui.show()
    splash.finish(gui)

    app.exec_()


if __name__ == '__main__':
    main()
