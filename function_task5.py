def calculateFactorial(num):
    factorial = 1
    if num < 0:
        print("Cannot calculate with negative number as input")
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        return factorial


num = int(input("Enter number - "))
print(calculateFactorial(num))