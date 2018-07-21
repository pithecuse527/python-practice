#
#
#   18.06.07
#   번호가 붙은 문장에서 번호를 빼고 output2.txt에 문장들을 저장.
#

infile = open("proverbs2.txt")
outfile = open("output2.txt", "w")

for line in infile:
    for word in line:
        if word not in "1234567890:":
            outfile.write(word)

infile.close()
outfile.close()
