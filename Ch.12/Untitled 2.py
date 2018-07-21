# -*- coding: utf8 -*-
import os.path
#import sys
#sys.setdefaultencoding("utf-8")

if os.path.isfile("phones.txt"):
    print("Already Exsisted file...")
else:
    outfile = open("phones.txt","w")
    outfile.write("Hong 010-1111-1111\n")
    outfile.write("Kim 010-1111-1111\n")
    outfile.write("Kim2 010-1111-1111\n")
    outfile.close()
