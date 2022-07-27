#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime


def getNow():
  """ get Now """
  today = datetime.datetime.now()
  return today.strftime("%Y-%m-%d %H:%M:%S")


