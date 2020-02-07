charCount = 1
char = '*'

for i in range(0, 5):
    print(char*charCount)
    charCount += 1
    if i == 4:
        charCount -= 1
        for l in range(0, 5):
            charCount -= 1
            print(char * charCount)