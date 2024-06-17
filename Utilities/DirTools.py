#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import subprocess
import sys
import shutil
import fnmatch
from pathlib import Path


class DirTools:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def pathEndingSlash(self, path):
        """check for ending slash at path"""
        if path.endswith(os.path.sep) is False:
            path = "%s%s" % (path, os.path.sep)
        return path

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

    def getSubDirs(self, rootdir):
        """get alls Subdirectories from rootdir, not recursive"""
        return [f.path for f in os.scandir(rootdir) if f.is_dir()]

    def getSubDirsRecursive(self, rootdir):
        subdirs = []
        for x in os.walk(rootdir):
            subdirs.append(x[0])
        return subdirs

    def search_files(self, directory=".", pattern=".*"):
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

    def search_files_in_dir(self, directory=".", pattern=""):
        """
        search for pattern in directory NOT recursive
        :param directory: path where to search. relative or absolute
        :param pattern: a list e.g. ['.jpg', '.gif']
        """
        data = []
        for child in Path(directory).iterdir():
            if child.is_file():
                # print(f"{child.name}")
                if pattern == "":
                    data.append(os.path.join(directory, child.name))
                else:
                    for p in pattern:
                        if child.name.endswith(p):
                            data.append(os.path.join(directory, child.name))
        return data

    def deleteDir(self, path):
        """delete a directory, even if it is not empty"""
        try:
            shutil.rmtree(path)
        except OSError as e:
            print("Error: %s : %s" % (path, e.strerror))

    def createDir(self, path):
        """create dir if it not exists"""
        if os.path.isdir(path) is False:
            os.mkdir(path)

    def openFileManager(self, path):
        """cross OS"""
        # MacOS
        if sys.platform == "darwin":
            subprocess.check_call(["open", path])
        elif sys.platform.startswith("linux"):
            subprocess.check_call(["xdg-open", path])
        elif sys.platform == "win32":
            subprocess.check_call(["explorer", path])
