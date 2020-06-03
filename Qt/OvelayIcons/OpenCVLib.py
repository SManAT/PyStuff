#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Stefan Hagmann

import cv2
import numpy as np
from PyQt5.Qt import QImage, qRgb
from PyQt5 import QtGui
from test import test_imghdr


class OpenCVLib(object):
    """
    for inspiration have a look at
    https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
    """

    def readPNG(self, img):
        """ preserver all channels """
        return cv2.imread(img, cv2.IMREAD_UNCHANGED)

    def QImage2MAT(self, qimg):
        """Converts a QImage into an opencv MAT format"""
        incomingImage = qimg.convertToFormat(4)  # RGB32
        width = incomingImage.width()
        height = incomingImage.height()

        ptr = incomingImage.bits()
        ptr.setsize(incomingImage.byteCount())
        arr = np.array(ptr).reshape(height, width, 4)  # copies the data
        return arr

    def MAT2QPixmap(self, cvImg):
        """ convert CV Image to QPixmap """
        return QtGui.QPixmap.fromImage(self.MAT2QImage(cvImg))

    def QImage2QPixmap(self, img):
        """ convert QImage to QPixmap """
        return QtGui.QPixmap.fromImage(img)

    def MAT2QImage(self, im, copy=False):
        """ convert CV MAT to QImage
        see https://gist.github.com/smex/5287589 """
        """
        Because OpenCV uses BGR order by default, you should first use
        cvtColor(src, dst, CV_BGR2RGB)
        to get an image layout that Qt understands
        """
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)  # important!
        gray_color_table = [qRgb(i, i, i) for i in range(256)]
        if im is None:
            return QImage()
        if im.dtype == np.uint8:
            if len(im.shape) == 2:
                qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_Indexed8)
                qim.setColorTable(gray_color_table)
                return qim.copy() if copy else qim

            elif len(im.shape) == 3:
                if im.shape[2] == 3:
                    qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_RGB888)
                    return qim.copy() if copy else qim
                elif im.shape[2] == 4:
                    qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_ARGB32)
                    return qim.copy() if copy else qim

    def resizeTo(self, img, width, height):
        """ resize the Mat to this width and height in px """
        h, w = img.shape[:2]
        fac_w = width / w
        fac_h = height / h
        # print("%s x %s" % (fac_w * w, fac_h * h))
        return cv2.resize(img, (int(fac_w * w), int(fac_h * h)), interpolation=cv2.INTER_CUBIC)
