firstNumber = int(input('Enter First number - '))
secondNumber = int(input('Enter Second number - '))
thirdNumber = int(input('Enter Third number - '))

def findMax(firstNumber, secondNumber, thirdNumber):
    max = -1000

    for i in range(0, 3):
        if (firstNumber > max):
            max = firstNumber

        if (secondNumber > max):
            max = secondNumber

        if (thirdNumber > max):
            max = thirdNumber

    return max

print(findMax(firstNumber, secondNumber, thirdNumber))