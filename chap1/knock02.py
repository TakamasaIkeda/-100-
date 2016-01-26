#!/usr/bin/env python
#-*- coding: utf-8 -*-

patcar = u"パトカー"
taxi = u"タクシー"

zipItems = zip(patcar, taxi)

for (a, b) in zipItems:
  print a + b

