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

        self.cv = OpenCVLib()
        self.CVTest(self.ui.image.pixmap())

    def closeEvent(self, event):
        ''' window tries to close '''
        # event.ignore()
        pass

    def CVTest(self, pixmap):
        Qimg = pixmap.toImage()
        img = self.cv.QImage2MAT(Qimg)
        # or load from file
        # image = cv2.imread("mexico.jpg")
        overlay = img.copy()
        output = img.copy()
        # red rectangle for demo
        cv2.rectangle(overlay, (420, 205), (595, 385), (0, 0, 255), -1)
        # apply the overlay
        # img, alpha, original, beta, gamma, output
        alpha = 0.5
        cv2.addWeighted(overlay, alpha, output, 1 - alpha, 1.0, output)
        # write back
        self.ui.image.setPixmap(self.cv.MAT2QPixmap(output))
        # Icon Test
        self.overlayIcon(self.ui.image.pixmap(), "test/ok.png")
        
        
    def copyROI(self, srcMat, dstMat, x, y):
        """ using ROI = region of interest to copy region """
        height, width = srcMat.shape[:2]
        # left upper corner x1, y1, right bottom corner x2, y2
        # y1:y2, x1:x2
        roi = srcMat[0:height, 0:width]

        # make both 3 channels RGB
        # roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGBA)
        # dstMat = cv2.cvtColor(dstMat, cv2.COLOR_BGR2RGB)

        #copy roi to dstMat
        # y1:y2, x1:x2
        dstMat[y:y + roi.shape[0], x:x + roi.shape[1]] = roi

        return dstMat
    
    def overlayIcon(self, pixmap, icon):
        Qimg = pixmap.toImage()
        img = self.cv.QImage2MAT(Qimg)
        output = img.copy()
        icon = self.cv.readPNG(icon)
        
        cv2.imshow('image', self.overlay_transparent(img, icon, 0, 0))



    def overlayIcon2(self, pixmap, icon):
        """ place icon onto pixmap """
        Qimg = pixmap.toImage()
        img = self.cv.QImage2MAT(Qimg)
        output = img.copy()
        icon = self.cv.readPNG(icon)

        cv2.imshow('icon', icon)

        icon = self.cv.resizeTo(icon, 64, 64)
        
        output = self.copyROI(icon, output, 10, 10)

     


        # write back
        self.ui.image.setPixmap(self.cv.MAT2QPixmap(output))
        
    def overlay_transparent(self, background_img, img_to_overlay_t, x, y, overlay_size=None):
        """
        Overlays a transparant PNG onto another image using CV2
        @param      background_img    The background image
        @param      img_to_overlay_t  The transparent image to overlay (has alpha channel)
        @param      x                 x location to place the top-left corner of our overlay
        @param      y                 y location to place the top-left corner of our overlay
        @param      overlay_size      The size to scale our overlay to (tuple), no scaling if None
        @return     Background image with overlay on top
        """
        bg_img = background_img.copy()
        if overlay_size is not None:
            img_to_overlay_t = cv2.resize(img_to_overlay_t.copy(), overlay_size)
        # Extract the alpha mask of the RGBA image, convert to RGB
        b, g, r, a = cv2.split(img_to_overlay_t)
        overlay_color = cv2.merge((b, g, r))
        # Apply some simple filtering to remove edge noise
        mask = cv2.medianBlur(a, 5)
        h, w, _ = overlay_color.shape
        roi = bg_img[y:y + h, x:x + w]
        # Black-out the area behind in our original ROI
        img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))
        # Mask out the logo from the logo image.
        img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)
        # Update the original image with our new ROI
        bg_img[y:y + h, x:x + w] = cv2.add(img1_bg, img2_fg)

        return bg_img


def main():
    app = QApplication(sys.argv)

    # show main Window
    gui = MAIN_UI()  #noqa
    gui.show()
    app.exec_()


if __name__ == '__main__':
    main()
