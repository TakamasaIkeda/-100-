#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

def line_count(filename):
  f = open(filename,"rb")
  for i,x in enumerate(f, start=1):
    pass
  f.close()
  return i 


if __name__ == "__main__":
  lines = line_count("hightemp.txt")
  print lines
