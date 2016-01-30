#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
"""

def merge(*files):
  col1 = open(files[0], "rb")
  col2 = open(files[1], "rb")
  new_file =  open("merge.txt", "wb")

  for i in zip(col1, col2): 
    line = i[0].strip("\n") + "\t" + i[1]
    new_file.write(line)

if __name__ == "__main__":
  file1 = "col1.txt"
  file2 = "col2.txt"
  merge(file1, file2)
