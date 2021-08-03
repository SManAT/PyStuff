#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import subprocess
import stat
import sys
import shutil
import fnmatch


class FileDirTools:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def countFiles(self, path):
        """count number of files and dirs in directory"""
        files_count = 0
        dir_count = 0
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                print(os.path.join(root, name))
            for name in dirs:
                print(os.path.join(root, name))
            files_count = len(files)
            dir_count = len(dirs)
        return [files_count, dir_count]

    def search_files(self, directory='.', pattern=''):
        """ search for pattern in directory recursive """
        data = []
        for dirpath, dirnames, files in os.walk(directory):
            for f in fnmatch.filter(files, pattern):
                data.append(os.path.join(dirpath, f))
        return data

    def deleteDir(self, path):
        """ delete a directory, even if it is not empty """
        try:
            shutil.rmtree(path)
        except OSError as e:
            print("Error: %s : %s" % (path, e.strerror))

    # File Operations -------------------------------------------------------------------

    def rmFile(self, filename):
        if (os.path.exists(filename) is True):
            os.remove(filename


    # Stuff -----------------------------------------------------------------------------
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
        st=os.stat(path)
        if octal == "777":
            mode=stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO
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
