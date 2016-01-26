#!/usr/bin/env python
#-*- coding: utf-8 -*-

#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

#与えられたcharに対するn-gramのlistを返す
def ngram(n, chars):
  charsList = [] 
  string = delspace(chars)
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

#和集合
def union(x, y):
 return x + y 

#積集合
def intersection(x, y):
  lists = union(x,y)
  return list(set(lists))

#差集合
def different(x, y):
  allList = set(union(x,y))
  partList = set(intersection(x,y))
  print allList
  print partList
  differenceList = partList.difference(allList)

  return list(differenceList)


if __name__ == "__main__":
  x = ngram(2, "paraparaparadise")
  y = ngram(2, "paragraph")
  print union(x, y)
  print intersection(x,y)
  print different(x,y)

  
