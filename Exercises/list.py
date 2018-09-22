# /usr/bin/env python3
# !-*-coding:utf-8-*-
l1 = ['hello', 'world', 18, 'apple', None]
l2 = []
for x in l1:
    if isinstance(x, str):
        l2.append(x)
    else:
        pass
print(l1)
print(l2)
