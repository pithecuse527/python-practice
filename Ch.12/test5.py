#
#
#   18.06.07
#   readlines()에서 s를 빼면 어떻게 출력이 되는가?
#

from tkinter import *
from tkinter.filedialog import askopenfilename

readFile = askopenfilename()
if readFile != None:
    infile = open(readFile, "r")

infile_ = infile.readlines()
#infile_ = infile.readline()          # s가 빠지면 한 줄만 읽어옴.
for line in infile_:
    line = line.strip()
    print(line)

infile.close()
