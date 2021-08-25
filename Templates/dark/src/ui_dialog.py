# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(470, 239)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(470, 239))
        Dialog.setMaximumSize(QSize(470, 239))
        Dialog.setStyleSheet(u"QMainWindow::separator\n"
"{\n"
"    background-color: #acacac;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    spacing: 2px;\n"
"    border: 1px dashed #76797C;\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: #787876;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #76797C;\n"
"    spacing: 2px;\n"
"}\n"
"QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #D1DBCB;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #232323;\n"
"    background-color: #acacac;\n"
"    selection-background-color:#acacac;\n"
"    selection-color: black;\n"
"    background-clip: border;\n"
"    border-image: none;\n"
"    border: 0px transparent black;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QWidget#border\n"
"{\n"
"  background-color: #232323;\n"
"}\n"
"\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #D1DBCB;\n"
"    color: black;\n"
"}\n"
"\n"
"QWidget:item:selec"
                        "ted\n"
"{\n"
"    background-color: #D1DBCB;\n"
"    border: 0px\n"
"}\n"
"\n"
"")
        self.gridLayout_5 = QGridLayout(Dialog)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.border = QWidget(Dialog)
        self.border.setObjectName(u"border")
        self.gridLayout = QGridLayout(self.border)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.content = QWidget(self.border)
        self.content.setObjectName(u"content")
        self.gridLayout_3 = QGridLayout(self.content)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.window_bar_outer = QWidget(self.content)
        self.window_bar_outer.setObjectName(u"window_bar_outer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.window_bar_outer.sizePolicy().hasHeightForWidth())
        self.window_bar_outer.setSizePolicy(sizePolicy1)
        self.window_bar_outer.setMinimumSize(QSize(0, 30))
        self.window_bar_outer.setMaximumSize(QSize(16777215, 30))
        self.window_bar_outer.setStyleSheet(u"background-color: #ffffff")
        self.window_bar_outerlayout = QHBoxLayout(self.window_bar_outer)
        self.window_bar_outerlayout.setObjectName(u"window_bar_outerlayout")
        self.window_bar_outerlayout.setContentsMargins(-1, 1, 4, 14)
        self.window_bar_inner = QFrame(self.window_bar_outer)
        self.window_bar_inner.setObjectName(u"window_bar_inner")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.window_bar_inner.sizePolicy().hasHeightForWidth())
        self.window_bar_inner.setSizePolicy(sizePolicy2)
        self.window_bar_inner.setMinimumSize(QSize(0, 30))
        self.window_bar_inner.setMaximumSize(QSize(16777215, 30))
        self.window_bar_inner.setFrameShape(QFrame.StyledPanel)
        self.window_bar_inner.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.window_bar_inner)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 2, 0, 0)
        self.title_bar = QFrame(self.window_bar_inner)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar_layout = QGridLayout(self.title_bar)
        self.title_bar_layout.setObjectName(u"title_bar_layout")
        self.title = QLabel(self.title_bar)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setBold(True)
        self.title.setFont(font)

        self.title_bar_layout.addWidget(self.title, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.title_bar)

        self.gridWidget_2 = QWidget(self.window_bar_inner)
        self.gridWidget_2.setObjectName(u"gridWidget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.gridWidget_2.sizePolicy().hasHeightForWidth())
        self.gridWidget_2.setSizePolicy(sizePolicy3)
        self.gridWidget_2.setMinimumSize(QSize(40, 0))
        self.gridWidget_2.setMaximumSize(QSize(40, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.gridWidget_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_close = QPushButton(self.gridWidget_2)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QSize(20, 20))
        self.btn_close.setStyleSheet(u"border: none; padding: 2px;")
        icon1 = QIcon()
        icon1.addFile(u":/qss_icons/themes/darkgray/icons/window_close_sw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setChecked(False)
        self.btn_close.setFlat(True)

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.gridWidget_2)


        self.window_bar_outerlayout.addWidget(self.window_bar_inner)


        self.gridLayout_3.addWidget(self.window_bar_outer, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.frame = QFrame(self.content)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, -1, 0, 0)
        self.message = QLabel(self.frame)
        self.message.setObjectName(u"message")
        font1 = QFont()
        font1.setPointSize(14)
        self.message.setFont(font1)
        self.message.setWordWrap(True)

        self.gridLayout_4.addWidget(self.message, 0, 1, 1, 1)

        self.icon = QLabel(self.frame)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(150, 0))
        self.icon.setMaximumSize(QSize(150, 16777215))
        self.icon.setFrameShape(QFrame.Panel)
        self.icon.setPixmap(QPixmap(u":/qss_icons/themes/darkgray/icons/warning.png"))

        self.gridLayout_4.addWidget(self.icon, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.content)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, -1, 10, 0)
        self.btn1 = QPushButton(self.frame_2)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setFont(font)
        self.btn1.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    color: #3b3b3b;\n"
"    text-shadow: 0 1px 1px #fff;\n"
"    box-shadow: 0 1px 0 #fff inset;\n"
"    font-size: 14px;\n"
"    line-height: 1.2;\n"
"    text-align: center;\n"
"    border-radius: 3px;\n"
"    padding: 5px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: #fabe32;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #e3e3e3;\n"
"}")

        self.gridLayout_2.addWidget(self.btn1, 0, 1, 1, 1)

        self.btn2 = QPushButton(self.frame_2)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setFont(font)
        self.btn2.setStyleSheet(u"QPushButton {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #ccc;\n"
"    color: #3b3b3b;\n"
"    text-shadow: 0 1px 1px #fff;\n"
"    box-shadow: 0 1px 0 #fff inset;\n"
"    font-size: 14px;\n"
"    line-height: 1.2;\n"
"    text-align: center;\n"
"    border-radius: 3px;\n"
"    padding: 5px 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: #fabe32;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #e3e3e3;\n"
"}")

        self.gridLayout_2.addWidget(self.btn2, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)


        self.gridLayout_3.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.content, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.border, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
        self.btn_close.setText("")
        self.message.setText(QCoreApplication.translate("Dialog", u"TextLabel\n"
"df\n"
"dfg", None))
        self.icon.setText("")
        self.btn1.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.btn2.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

