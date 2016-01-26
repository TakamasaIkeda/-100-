#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""
#問題の意味がよくわかんねーから(219 - asciiコード)にしとく


#英語の文章を受け取り, 暗号化された文字列を返す
def cipher(string):
  cipher = ""
  for i in string:
    if i.islower():
      cipher += str(219 - ord(i))
    else:
      cipher += i
  return cipher 

#暗号化された文字列を受け取り, 複合化された文字列を返す
def decryption(encrypt):
  decrypt = ""
  for i in encrypt:
    if i.isupper():
      decrypt += str(i)
    else:
      decrypt += chr(i)

  return  decrypt 


if __name__ == "__main__":
  string = u"Hi yoh"
  encrypt = cipher(string)

  decrypt = decryption(encrypt)
  print decrypt
