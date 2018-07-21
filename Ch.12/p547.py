infile = open("phones.txt", "r")
for line in infile.readlines():
    line = line.strip()
    print(line)
infile.close()
