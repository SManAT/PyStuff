#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import subprocess
import stat
import sys
import shutil
import fnmatch


class DirTools:
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

    def search_files(self, directory='.', pattern='.*'):
        """
        search for pattern in directory recursive
        :param directory: path where to search. relative or absolute
        :param pattern: a list e.g. ['*.jpg', '__.*']
        """
        data = []
        for dirpath, dirnames, files in os.walk(directory):
            for p in pattern:
                for f in fnmatch.filter(files, p):
                    data.append(os.path.join(dirpath, f))
        return data

    def deleteDir(self, path):
        """ delete a directory, even if it is not empty """
        try:
            shutil.rmtree(path)
        except OSError as e:
            print("Error: %s : %s" % (path, e.strerror))

    def createDir(self, path):
        """ create dir if it not exists """
        if os.path.isdir(path) is False:
            os.mkdir(path)

    def openFileManager(self, path):
        """ cross OS """
        # MacOS
        if sys.platform == 'darwin':
            subprocess.check_call(['open', path])
        elif sys.platform.startswith('linux'):
            subprocess.check_call(['xdg-open', path])
        elif sys.platform == 'win32':
            subprocess.check_call(['explorer', path])
