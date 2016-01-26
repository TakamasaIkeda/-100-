#!/usr/bin/env python
#-*- coding: utf-8 -*-

def answer(x, y, z):
  string = str(x) + "時の" + y + "は" + str(z)
  return string 


if __name__ == "__main__":
  x = 12
  y = "気温"
  z = 22.4
  print answer(x, y, z)
