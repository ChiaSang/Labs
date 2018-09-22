grade = int(input("请输入分数！\n"))
if grade > 90 and grade < 100:
    print("你的成绩为A")
elif grade > 70 and grade < 89:
    print("你的成绩为B")
elif grade > 0 and grade < 69:
    print("你的成绩为C")
elif grade > 0 and grade < 59:
    print("你的成绩为D")
else:
    print("Invalid score!\n")
# 打印成绩