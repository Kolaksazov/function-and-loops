checkForBlankLine = False
userInput = input()

while(checkForBlankLine == False):
    if not userInput.strip():
        print('You entered a blank line..')
        checkForBlankLine = True
    else:
        print(str(userInput).lower())
        userInput = input()