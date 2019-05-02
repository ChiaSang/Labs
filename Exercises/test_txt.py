def find_word(filename,word):
    flag = False
    with open(filename, 'r') as f:
        for l in f.readlines():
              if word in l:
                  flag = True
                  break
    print(flag)
    return flag
find_word('D:/Documents/Python/Exercises/filter.txt', 'ee/onsta')