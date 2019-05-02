import random
number = []
office = [[], [], []]
teacher = ['老张', '老王', '老刘', '老李', '老邢', '老张', '老王', '老刘', '老李', '老邢']
for temp in teacher:
    index = random.randint(0, 2)
    number = office[index].append(temp)
    print(number)
print("办公室人员分别为：")
i = 1
for temp2 in office:
    print("-" * 20)
    print("办公室：", i)
    print("-" * 20)
    for temp3 in temp2:
        print(temp3)
    i += 1
