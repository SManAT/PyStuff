#! /usr/bin/env python
# -*- coding: utf-8 -*-


class StringTools:
  def __init__(self):
    self.logger = logging.getLogger(__name__)

  def normalize(self, thestr):
      """ replace some Problem characters """
      patterns = {
        'ä': 'ae',
        'ö': 'oe',
        'ü': 'ue',
        'ß': 'ss',
        'é': 'e',
        'è': 'e',
        'ê': 'e',
        'ë': 'e',
        'á': 'a',
        'à': 'a',
        'â': 'a', 
        'î': 'i',
        'ï': 'i',
        'ç': 'c',
        'ú': 'u',
        'ù': 'u',
        'û': 'u',
        'ò': 'o',
        'ó': 'o',
        'ô': 'o',
      }
      thestr = str(thestr)
      for key, val in patterns.items():
        thestr = thestr.replace(key, val)
      return thestr

  