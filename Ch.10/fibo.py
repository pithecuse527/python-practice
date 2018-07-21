#
#
#   18.05.17
#   피보나치 수열
# 

def fib(n):         # 피보나치 수열 출력 (매개변수 n까지)
    a,b = 0,1
    while b < n:
        print(b, end=' ')
        a,b = b, a+b
    print()

def fib2(n):        # 피보나치 수열 리스트 반환
    a,b = 0,1
    result = []
    while b < n:
        result.append(b)
        a,b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
