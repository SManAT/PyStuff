import sys

from pathlib import Path
from src.controllers.Database import Database
import os
from src.config.LoggerConfiguration import configure_logging
from src.controllers.Users import Users
from ui_main import Ui_MainWindow
from src.ui_Functions import ui_Functions
from PySide6.QtWidgets import QMainWindow, QApplication
import yaml
import logging
from PySide6 import QtGui, QtCore
from Dialog import Dialog


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.logger = logging.getLogger('MainWindow')
        self.ui = Ui_MainWindow()
        self.rootDir = Path(__file__).parent
        self.dbDir = os.path.join(self.rootDir, "db")
        self.configFile = os.path.join(self.rootDir, 'src', 'config', 'config.yaml')
        self.config = self.load_yml()

        # UI Stuff
        self.ui.setupUi(self)
        self.ui_functions = ui_Functions(self, self.ui)
        self.ui_functions.setWindowTitle(self.config['app']['title'])
        self.setWindowIcon(QtGui.QIcon(os.path.join(self.rootDir, 'App.ico')))

        # Connectors
        self.ui.btn_close.clicked.connect(self.window_close)
        self.ui.btn_max.clicked.connect(self.ui_functions.maximize_restore)
        self.ui.btn_min.clicked.connect(self.showMinimized)

        # Database Setup --------------------------
        self.db = Database(self.dbDir)

        # Setup Tables ----------------------------
        table_user = Users(self, "users")
        table_user.setup()

        QtCore.QTimer.singleShot(500, lambda: self.test())

    def test(self):
        """ only a Test Situation """
        dialog = Dialog()
        self.ui_functions.showDialog(dialog, "Information",
                                     "Heute ist ein \n schöner Tag",
                                     "warning",
                                     "Cancel",
                                     "OK")
        # which Button was pressed
        if dialog.leftButton is True:
            print("Left")
        if dialog.rightButton is True:
            print("Right")

    def closeEvent(self, event):
        """ catch the closing Event """
        print("X is clicked: I'm now closing ...")

    def createEmptyConfigFile(self):
        """ will create an Empty Config File """
        data = dict(
            app=dict(
                title='MyApp',
            ),
            azure=dict(
                client_id='xxxx',
                client_secret='xxx',
                tenant_id='xxx',
            )
        )
        with open(self.configFile, 'w') as f:
            yaml.dump(data, f, sort_keys=False, default_flow_style=False)

    def load_yml(self):
        """ Load the yaml file config.yaml """
        if os.path.exists(self.configFile) is False:
            self.createEmptyConfigFile()
            self.logger.error("New config.yml File created ...")
            self.logger.error("Please edit src/config/config.yml as needed ...")
            self.logger.error("- Exit -")
            sys.exit(-1)
        with open(self.configFile, 'rt') as f:
            yml = yaml.safe_load(f.read())
        return yml

    def window_close(self):
        """ exit the app """
        app.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    configure_logging()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
