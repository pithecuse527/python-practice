outfile = open("phones.txt", "a")

outfile.write("Choi 010-1234-1234\n")
outfile.write("Choi22 010-1234-1234\n")
outfile.close()

outfile = open("phones.txt", "r")
for line in outfile:
    print(line.rstrip())
outfile.close()
