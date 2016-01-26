#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""09.暗号文
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
split_sentence = sentence.split(" ")

processed_sentence = list()
#空白で区切った文字列リストに対し, 4文字以下ならそのままリストにappend, それ以外なら先頭と末尾の文字を入れ替えてappend
for i in split_sentence:
  if(len(i) <= 4):
    processed_sentence.append(i)
  else:
    head = i[-1] 
    tail = i[:1] 
    middle = i[1:-1]
    new_word = head + middle + tail
    processed_sentence.append(new_word)

for i in processed_sentence:
  print i

