from src.ui_dialog import Ui_Dialog
from PySide6.QtWidgets import QDialog
from PySide6 import QtCore
from PySide6.QtGui import QPixmap


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        # UI Stuff
        self.ui.setupUi(self)

        # Frameless
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Connectors
        self.ui.btn1.clicked.connect(self.btn1Clicked)
        self.ui.btn2.clicked.connect(self.btn2Clicked)

        self.leftButton = False
        self.rightButton = False

    def setTitle(self, msg):
        """ set the title """
        self.ui.title.setText(msg)

    def setMessage(self, msg):
        """ set the message """
        self.ui.message.setText(msg)

    def setBtn1(self, txt):
        """ set Text for Button 1 """
        self.ui.btn1.setText(txt)

    def setBtn2(self, txt):
        """ set Text for Button 2 """
        self.ui.btn2.setText(txt)

    def setIcon(self, icon):
        """
        set the Icon from Resource
        :param icon: warning|notice|error|success
        """
        if "warning" in icon:
            iname = "warning.png"
        elif "notice" in icon:
            iname = "notice.png"
        elif "error" in icon:
            iname = "error.png"
        elif "success" in icon:
            iname = "success.png"

        self.ui.icon.setPixmap(QPixmap(":/qss_icons/themes/darkgray/icons/%s" % iname))

    def btn1Clicked(self):
        """ Button1 was clicked """
        self.leftButton = True
        self.close()

    def btn2Clicked(self):
        """ Button2 was clicked """
        self.rightButton = True
        self.close()
