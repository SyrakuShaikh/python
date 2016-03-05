while True:
    s = int(input('Enter a number : '))
    if s:
        print('true block')
    else:
        print('false block')

    if s == 42:
        break
    print('Something test for break', s)
print('Done')
