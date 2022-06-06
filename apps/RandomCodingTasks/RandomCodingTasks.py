#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Copyright (C) Mag. Stefan Hagmann 2021

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import click
import yaml

from pathlib import Path
from libs.Tool import Tool


class RandomCodingTasks():
    """ Random select a Number """
    debug = False

    def __init__(self, file, count, save, clear):
        self.rootDir = Path(__file__).parent
        self.configFile = os.path.join(self.rootDir, 'config.yaml')

        self.file = file
        self.count = count
        self.save = save
        self.clear = clear

        self.config = self.load_yml()
        self.config['root'] = self.rootDir
        info = ("\nCreate Random Tasks for students, (c) Mag. Stefan Hagmann 2021\n"
                "-------------------------------------------------------\n")
        print(info)

    def load_yml(self):
        """ Load the yaml file config.yaml """
        with open(self.configFile, 'rt') as f:
            yml = yaml.safe_load(f.read())
        return yml

    def start(self):
      tool = Tool(self.config, self.file, self.count, self.save, self.clear)
      tool.start()


@click.command()
@click.option('-f', '--file', required=True, help='which students CSV file to use')
@click.option('-c', '--count', default=1, help='How many tasks to create')
@click.option('-s', '--save', is_flag=True, help='Save it')
@click.option('-cl', '--clear', is_flag=True, help='Clear stored Taks')
def start(file, count, save, clear):

    if file is False:
      ctx = click.get_current_context()
      print(ctx.get_help())
      exit(-1)

    tasks = RandomCodingTasks(file, count, save, clear)
    tasks.start()


if __name__ == "__main__":
    start()
