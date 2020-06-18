#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Stefan Hagmann
import sys
from PyQt5.QtWidgets import QApplication
from Qt.ConnectionStatus.ConnectionStatus import ConnectionStatus


def close_app():
    QApplication.quit()


def printhelp():
    msg = '''
python3 ConnectionStatusDispatcher.py type
    1 ... connected
    something else = NOT connected

example:
python3 ConnectionStatusDispatcher.py 1
'''
    print(msg)
    sys.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #if len(sys.argv) != 2:
    #    print("Argument mismatch...")
    #    printhelp()
    #typ = sys.argv[1]
    typ = 1

    status = ConnectionStatus()
    status.setType(typ)
    status.show()
    

    app.exec_()
