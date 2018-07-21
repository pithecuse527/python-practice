import os

def calcDirSize(name):
    totalSize = 0

    if os.path.isfile(name):
        totalSize += os.path.getsize(name)
    else:
        fileList = os.listdir(name)
        for subDir in fileList:
            if subDir != ".DS_Store":
                totalSize += calcDirSize(name + "/" + subDir)
    return totalSize

name = input("디렉터리 이름을 입력하시오 : ")
print(calcDirSize(name))
