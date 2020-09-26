with open('d:\\fp.txt', 'rt') as file1:
    sentence = file1.readlines()
    for i in range(0, len(sentence)):
        sentence[i] = str(i + 1) + ' ' + sentence[i]
with open('d:\\fp2.txt', 'wt') as file2:
    file2.writelines(sentence)
