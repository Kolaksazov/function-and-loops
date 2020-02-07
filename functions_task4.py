sampleString = '1234abcd'

def reverseString(sampleString):
    resultString = ''
    for character in sampleString:
        resultString = character + resultString

    return resultString

print(reverseString(sampleString))