#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Stefan Hagmann

import numpy as np
from PyQt5.Qt import QImage, qRgb
from PyQt5 import QtGui


class OpenCVLib(object):

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
