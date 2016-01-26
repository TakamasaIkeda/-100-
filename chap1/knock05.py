#!/usr/bin/env python
#-*- coding: utf-8 -*-

#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

def ngram(n, chars):
  charsList = [] 
  string = delspace(chars)
  print string
  for (i,x) in enumerate(string):
    gram = string[i:i+n:]
    charsList.append(gram)

  return charsList

def delspace(chars):
  chars = chars.split(" ")
  string = ""
  for i in chars:
    string += i
  return string


if __name__ == "__main__":
  chars = u"I am an NLPer"
  print ngram(2,chars)

  
