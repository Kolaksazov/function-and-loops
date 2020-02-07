sampleList = [8, 2, 3, 0, 7]

def sumList(sampleList):
    result = 0

    for element in sampleList:
        result += element

    return result

print(sumList(sampleList))