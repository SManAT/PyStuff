#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import stat
import sys
import subprocess
from pathlib import Path


class FileTools:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def rmFile(self, filename):
        if (os.path.exists(filename) is True):
            os.remove(filename)

    def getFileExtension(self, filename):
        """ get Extension of a File without . """
        return os.path.splitext(filename)[1][1:].strip().lower()

    def getFilename(self, filename):
        """ get the filename only, without extension """
        return Path(filename).stem

    def changePermission(self, path, octal):
        """
        change the permission to ... see man 2 open
        stat.S_ISUID − Set user ID on execution.
        stat.S_ISGID − Set group ID on execution.
        stat.S_ENFMT − Record locking enforced.
        stat.S_ISVTX − Save text image after execution.
        stat.S_IREAD − Read by owner.
        stat.S_IWRITE − Write by owner.
        stat.S_IEXEC − Execute by owner.
        stat.S_IRWXU − Read, write, and execute by owner.
        stat.S_IRUSR − Read by owner.
        stat.S_IWUSR − Write by owner.
        stat.S_IXUSR − Execute by owner.
        stat.S_IRWXG − Read, write, and execute by group.
        stat.S_IRGRP − Read by group.
        stat.S_IWGRP − Write by group.
        stat.S_IXGRP − Execute by group.
        stat.S_IRWXO − Read, write, and execute by others.
        stat.S_IROTH − Read by others.
        stat.S_IWOTH − Write by others.
        stat.S_IXOTH − Execute by others.
        """
        st = os.stat(path)
        if octal == "777":
            mode = stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO
        os.chmod(path, st.st_mode | mode)

    def openFileManager(self, path):
        """ cross OS """
        # MacOS
        if sys.platform == 'darwin':
            subprocess.check_call(['open', path])
        elif sys.platform.startswith('linux'):
            subprocess.check_call(['xdg-open', path])
        elif sys.platform == 'win32':
            subprocess.check_call(['explorer', path])
