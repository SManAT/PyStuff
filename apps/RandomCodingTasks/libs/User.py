class User():
  """ single User Object """
  vorname = ""
  nachname = ""
  klasse = ""

  def __init__(self):
    pass

  def __str__(self):
    return "%s %s" % (self.vorname, self.nachname)

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
    return "%s %s %s" % (self.getNachname(), self.getVorname(), self.getKlasse())
