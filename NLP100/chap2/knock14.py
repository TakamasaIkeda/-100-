#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""
from sys import argv

argc = len(argv)

def show_lines(filename):
  """ファイル名を受け取り先頭N行目までを表示"""
  f = open(filename, "rb")
  head = int(argv[1])

  for i,x in enumerate(f):
    if(i == head):
      break
    print x


if __name__ == "__main__":
  filename = "hightemp.txt"    
  if(argc is not 2):
    print("引数の数がちゃうで")
  else:
    show_lines(filename)
