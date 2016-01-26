#!/usr/bin/env python
#-*- coding: utf-8 -*-

""""Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""


headNumber = [1,5,6,7,8,9,15,16,19]
charDict = {}
sentense = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
splitSentense = sentense.split(" ")

for (number, item) in enumerate(splitSentense):
  if number in headNumber:
    firstChar = item[0:1]
    charDict[firstChar] = number
  else:
    secondChar = item[0:2]
    charDict[secondChar] = number

print charDict

    
