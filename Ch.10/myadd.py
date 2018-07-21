def sumToN(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

if __name__ == "__main__":
    import sys
    sum(int(sys.argv[1]))
