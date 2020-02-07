number = int(input('Write the number - '))
firstRange = int(input('Specify the first number of the range - '))
secondRange = int(input('Specify the second number of the range - '))

def checkIfNumberIsInRange(number, firstRange, secondRange):
    if number in range(firstRange, secondRange):
        print('Number is in the given range')
    else:
        print('Number is not in this range')


checkIfNumberIsInRange(number, firstRange, secondRange)