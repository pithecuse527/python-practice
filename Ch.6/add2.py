def add(num1, op, num2) :
    if op == '+' :
        return num1 + num2
    elif op == '-' :
        return num1 - num2
    elif op == '/' :
        return num1 / num2
    elif op == '*' :
        return num1 * num2
    else :
        return "Invalid operator!"


if __name__ == "__main__" :
    import sys
    print(add(float(sys.argv[1]), sys.argv[3], float(sys.argv[2])))
