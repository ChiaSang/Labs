spam = ['apple', 'bananas', 'tofu', 'cats']


def addand(spam):
    spam.insert((len(spam) - 1), 'and')
    print("结果为")
    print(','.join(spam))

spam = []
length = int(input("请输入列表的长度\n"))
for i in range(length):
    print("请输入第%d个字符" % (i + 1))
    spam.append(input())
addand(spam)
