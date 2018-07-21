#-*- coding: utf-8 -*-
infile = open("proverbs.txt", "r+")
str = infile.read(10)
print("읽은 문자열 : ", str)
position = infile.tell()
print("현재 위치 : ", position)

position = infile.seek(0, 0)
str = infile.read(10)
print("다시 읽은 문자열 : ", str)
infile.close()
