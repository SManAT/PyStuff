#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Stefan Hagmann
import sys
from pathlib import Path
import PyQt5
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from Qt.OvelayIcons.OpenCVLib import OpenCVLib
import cv2


class MAIN_UI(PyQt5.QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MAIN_UI, self).__init__(parent)
        self.rootDir = Path(__file__).parent
        uifile = self.rootDir.joinpath('main.ui')
        self.ui = uic.loadUi(uifile, self)        # load UI inside QMainWindow

        self.CVTest()

    def closeEvent(self, event):
        ''' window tries to close '''
        # event.ignore()
        pass

    def CVTest(self):
        cv = OpenCVLib()
        Qimg = self.ui.image.pixmap().toImage()
        img = cv.QImage2MAT(Qimg)
        # or load from file
        # image = cv2.imread("mexico.jpg")
        overlay = img.copy()
        output = img.copy()
        # red rectangle for demo
        cv2.rectangle(overlay, (420, 205), (595, 385), (0, 0, 255), -1)
        # apply the overlay
        # img, alpha, original, beta, gamma, output
        alpha = 1
        cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
        # write back
        self.ui.image.setPixmap(cv.MAT2QPixmap(output))


def main():
    app = QApplication(sys.argv)

    # show main Window
    gui = MAIN_UI()  #noqa
    gui.show()
    app.exec_()


if __name__ == '__main__':
    main()
