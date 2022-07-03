
def readInteger(msg):
  hasErrors =True
  while hasErrors is True:
      try:
          print(msg, sep='', end='')
          number = eval(input())
          hasErrors =False
      except:
          print(">> not a number ... try again")
  return number

def getSizeofDict(dict):
  i = 0
  data = self.processList(dict) 
  for key, item in data.items():
      i += 1
  return i
