#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""

def replace_tab(filename):
  f = open(filename, "rb")
  space = " "
  tab = "\t"

  for i,x in enumerate(f):
    if(tab in x):
      replaced = x.replace(tab, space)
      print(replaced)

    if(i == len(x) - 1):
      break
  f.close()

if __name__ == "__main__":
  lines = replace_tab("hightemp.txt")
