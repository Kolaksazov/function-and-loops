sampleList = [8, 2, 3, -1, 7]

def multiplyList(sampleList):
    result = 1

    for element in sampleList:
      result *= element

    return result

print(multiplyList(sampleList))