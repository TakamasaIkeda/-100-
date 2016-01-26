#!/usr/bin/env python
#-*- coding: utf-8 -*-

firstCharacter = []
sentense = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
splitSentense = sentense.split(" ")
for (number, item) in enumerate(splitSentense):
  print item + " " +  item[0:1]
  firstCharacter.append(item[0:1])
  
print firstCharacter

    
