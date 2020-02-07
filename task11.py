i = 4
j = 3
Matrix = [[0 for x in range(i)] for y in range(j)]

for first in range(0, j):
    for second in range(0, i):
        Matrix[first][second] = first*second

print(Matrix)