#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""

def line_count(filename):

  f = open(filename,"rb")
  col1 = open("col1.txt", "wb")
  col2 = open("col2.txt", "wb")


  for i,x in enumerate(f):
    if(i%2 == 0):
    #col1.txtへ
      col1.write(x)
    else:
    #col2.txtへ
      col2.write(x) 

  f.close()
  col1.close()
  col2.close() 


if __name__ == "__main__":
  lines = line_count("hightemp.txt")
