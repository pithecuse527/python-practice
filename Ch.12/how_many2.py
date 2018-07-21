filename = input("파일명 입력 : ").strip()
infile = open(filename, "r")

freqs = {}

for line in infile:
    words = line.split()
    for word in words:
        if word.strip() in freqs:
            freqs[word] += 1
        else:
            freqs[word] = 1
print(freqs)
infile.close()
