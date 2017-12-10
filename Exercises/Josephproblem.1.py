# mylist = range(1, 11)
# del_num = []
# x = 0
# i = 0
# while len(del_num) < 11:
#     if x > 10:
#         x = 0
#     if (mylist[i] not in del_num):
#         i = i + 1
#         if (i % 2 == 0):
#             print(mylist[x])
#             del_num.append(mylist[x])
#             i = 0
#     x = x + 1
"""
一百个坏蛋，每次杀死奇数号的，最后剩下谁呢？
"""


def kill_them(bad_gays):
    """
    因为索引从零开始，所以每次清除索引为偶数的bad_gay
    """
    bad_gays = [gay for gay in bad_gays if bad_gays.index(gay) % 2 != 0]
    print(bad_gays)
    return kill_them(bad_gays) if len(bad_gays) != 1 else bad_gays


if __name__ == "__main__":
    bad_gays = [gay for gay in range(1, 101)]
    print("start:", bad_gays)
    the_last_one = kill_them(bad_gays)
    print("end", the_last_one)
