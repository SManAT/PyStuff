# https://realpython.com/python-csv/#parsing-csv-files-with-the-pandas-library

import os
import pandas
from libs.User import User


class CSVTool():
  """ Read / Write CSV Files with pandas """
  userList = []

  def __init__(self):
    pass

  def getUsers(self):
    """ return all Users from CSV File """
    return self.userList

  def read(self, filename):
    """ Read a CSV file """
    self.userList.clear()

    if os.path.exists(filename) is True:
      df = pandas.read_csv(filename)

      for index, row in df.iterrows():
        user = User()
        try:
          user.setVorname(str(row['Vorname']).strip())
          user.setNachname(str(row['Nachname']).strip())
          user.setKlasse(str(row['Klasse']).strip())

          self.userList.append(user)
        except Exception as ex:
          self.logger.error("Parsing csv File Error, is the seperator , ?")
          print(ex)
    else:
      self.logger.error("File ./%s not found! - exit -" % filename)

  def write(self, filename, data):
    """ Write data to a CSV File """
    df = pandas.read_csv('hrdata.csv',
                         index_col='Employee',
                         parse_dates=['Hired'],
                         header=0,
                         names=['Employee', 'Hired', 'Salary', 'Sick Days'])
    df.to_csv('hrdata_modified.csv')
