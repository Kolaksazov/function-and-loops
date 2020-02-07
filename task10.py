for i in range(1, 51):

    if (i % 3 == 0):
        if (i % 5 == 0):
            print('FizzBuzz')
            continue
        else:
            print('Fizz')
            continue

    if (i % 5 == 0):
        print('Buzz')
        continue

    print(i)

