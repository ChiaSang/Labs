while True:
    sum = 0
    str = input('please inter a number\n')
    if (str == 'quit'):
        break
    else:
        for i in range(1, len(str)):
            sum = sum + int(str[i])
        if sum == int(str[0]):
            print('Yeah it is\n')
        else:
            print('Can not find it\n')
