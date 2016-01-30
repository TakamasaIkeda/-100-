#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""

def append_data(filename):

  f = open(filename,"rb")
  col1 = open("col1.txt", "wb")
  col2 = open("col2.txt", "wb")

  
  for i in f:
    split_line = i.split("\t")
    col1.write(split_line[0] + "\n")
    col2.write(split_line[1] + "\n")



  f.close()
  col1.close()
  col2.close() 


if __name__ == "__main__":
  append_data("hightemp.txt")
