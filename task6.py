numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

oddCount = 0
evenCount = 0

for i in numbers:
    if (i % 2 == 0):
        evenCount += 1
    else:
        oddCount += 1

print("Number of even numbers: ", evenCount)
print("Number of odd numbers: ", oddCount)
