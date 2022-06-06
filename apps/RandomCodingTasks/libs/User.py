class User():
  """ single User Object """
  vorname = ""
  nachname = ""
  klasse = ""

  def __init__(self):
    pass

  def __str__(self):
    return "%s %s %s" % (self.vorname, self.nachname, self.getKlasse())

  def setVorname(self, str):
    self.vorname = str

  def setNachname(self, str):
    self.nachname = str

  def setKlasse(self, str):
    self.klasse = str

  def getVorname(self):
    return self.vorname

  def getNachname(self):
    return self.nachname

  def getKlasse(self):
    return self.klasse

  def getFullname(self):
    return "%s %s" % (self.getNachname(), self.getVorname())

  def asDict(self):
    """ return as Dictionary """
    return {'vorname': self.getVorname(), 'nachname': self.getNachname(), 'klasse': self.getKlasse()}
