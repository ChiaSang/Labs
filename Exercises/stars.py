for i in range(0, 11):
    print('*' * i)
print('-' * 20)
# ----------------------------------
for j in range(0, 11):
    s = ''
    for q in range(0, 10 - j):
        s += '-'
    for q in range(0, 2 * j - 1):
        s += '*'
    print(s)
