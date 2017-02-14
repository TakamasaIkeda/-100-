#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""

from sys import argv

argc = len(argv)

def split_lines(filename):
  """ファイル名を受け取り末尾N行目までを表示(末尾から)"""
  f = open(filename, "rb")
  
  split = int(argv[1])
  lists = list()

  #一度全要素をlistへappend
  for x in f:
    lists.append(x)
  
  for i,x in enumerate(lists):
    if(i%split == 0):
      for j in xrange(split):
        print(lists[i+j])
      print("----------")

if __name__ == "__main__":
  filename = "hightemp.txt"    
  if(argc is not 2):
    print("引数の数がちゃうで")
  else:
    split_lines(filename)
