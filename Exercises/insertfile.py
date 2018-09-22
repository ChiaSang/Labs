with open('d:\\fp.txt', 'rt') as file1:
    s = file1.read()
    a = s.split('\n')
    insertinfo = ['Name:Blowin in the wind', 'Artist:Bob Dylan']
    for j in range(0, 1):
        for i in insertinfo:
            a.insert(j, i)
    s = '\n'.join(a)
    file1.close()
s = '1962 by Warner Bros. Inc.'
with open('d:\\fp.txt', 'a+') as file3:
    file3.writelines('\n', s)
with open('d:\\fp.txt', 'wt') as file2:
    file2.write(s)
    file2.close()
for line in open('d:\\fp.txt'):
    print(line)
