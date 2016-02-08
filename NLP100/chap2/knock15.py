#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""
from sys import argv

argc = len(argv)

def show_lines_rev(filename):
  """ファイル名を受け取り末尾N行目までを表示(末尾から)"""
  f = open(filename, "rb")
  tail = int(argv[1])
  lists = list()

  #一度全要素をlistへappend
  count = 0
  for x in f:
    lists.append(x)
    count += 1
  
  for i,x in enumerate(range(tail), start=1):
    print(lists[-i])
  
def show_lines(filename):
  """ファイル名を受け取り末尾N行目までを表示"""
  f = open(filename, "rb")
  tail = int(argv[1])
  lists = list()

  #一度全要素をlistへappend
  count = 0
  for x in f:
    lists.append(x)
    count += 1

  index = count - tail
  
  for i,x in enumerate(lists, start=1):
    if(i>index):
      print(x)


if __name__ == "__main__":
  filename = "hightemp.txt"    
  if(argc is not 2):
    print("引数の数がちゃうで")
  else:
    show_lines(filename)
