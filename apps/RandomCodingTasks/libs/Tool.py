import os
import random

from libs.CSVTool import CSVTool
from libs.DictTools import DictTools


class Tool():
    def __init__(self, config, file, count, save, clear):
        self.config = config
        self.file = file
        self.count = count
        self.save = save
        self.clear = clear
        self.dictTools = DictTools()

        self.dict = {}
        self.filename = 'storage.yaml'

    def start(self):
        self.csv = CSVTool()
        self.loadKlassen()
        if self.clear == False:
          self.createRandomTasks()
        else:
          self.clearDict()

    def loadKlassen(self):
      """ Import Users from CSV File """
      self.csv.read(self.file)

    def getTasks(self, list):
      """ get numbers from string """
      parts = list.split(' ')
      erg = []
      for number in parts:
        try:
          erg.append(int(number.strip()))
        except:
          pass
      return erg

    def inUserTasks(self, usertasks, task):
        """ doese the user already have made this task number? """
        found = False
        for item in usertasks:
          if task == item:
            found = True
            break
        return found

    def createTasksString(self, tasks):
      """ create String from list """
      erg = ""
      for item in tasks:
        erg = erg + str(item) + " "

      return erg[:-1]

    def createRandomTasks(self):
      # how many tasks do we have
      overall = self.config['tasks']['overall']
      filename = os.path.join(self.config['root'], self.filename)

      for user in self.csv.getUsers():
        self.dict[user.getFullname()] = user.asDict()

      # read old Data
      self.storedDict = self.dictTools.read(filename)
      for key, data in self.storedDict.items():
        try:
          self.dict[key]['tasks'] = data['tasks']
        except KeyError:
          self.dict[key]['tasks'] = ''

      # create Random Tasks
      for key, data in self.dict.items():
        usertasks = self.getTasks(data['tasks'])

        for i in range(0, self.count):
          task = random.randint(1, overall)
          while self.inUserTasks(usertasks, task):
            task = random.randint(1, overall)
          usertasks.append(task)
        # store it to global dict
        self.dict[key]['tasks'] = self.createTasksString(usertasks)

      for key, data in self.dict.items():
        # :<25 box with 25 chars length
        print(f"{self.dict[key]['nachname']} {self.dict[key]['vorname'] :<15} {self.dict[key]['tasks']}")

      # create random tasks, that the user doese not got already
      if self.save:
        print("\nSaving to %f" % self.filename)
        self.dictTools.write(self.dict, filename)
      else:
        print("\nTasks not saved ... !")

    def clearDict(self):
      """ clear stored tasks """
      # read old Data
      filename = os.path.join(self.config['root'], self.filename)
      self.dict = self.dictTools.read(filename)
      for key, data in self.dict.items():
        self.dict[key]['tasks'] = ''

      print("\nSaving Data cleared, no tasks are stored ...")
      self.dictTools.write(self.dict, filename)
