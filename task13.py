string = 'Python 3.2'
numberOfLetters = 0
numberOfDigits = 0

for char in string:
    if (char.isalpha()):
        numberOfLetters += 1

for digit in string:
    if (digit.isdigit()):
        numberOfDigits += 1

print('Letters', numberOfLetters)
print('Digits', numberOfDigits)