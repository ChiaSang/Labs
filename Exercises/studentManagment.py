import sys
studentinfo = {}
studentName = []
print("学生管理系统 v0.1")
print("0退出系统")
print("1添加学生信息")
print("2删除学生信息")
print("3修改学生信息")
print("4查询学生信息")
print("-" * 20)
while True:
    No = int(input("请选择功能\n"))
    if No == 0:
        print("退出")
        sys.exit()
    elif No == 1:  # 做一个循环，依次输入信息。判断每次输入的字符是不是exit，如果是则跳出循环
        while True:
            inputinfo = input("请依次输入学生的ID，姓名，性别，年龄")
            if inputinfo != exit:
                studentinfo['id'] = inputinfo
                studentinfo['name'] = inputinfo
                studentinfo['sex'] = inputinfo
                studentinfo['age'] = inputinfo
            else:
                break
    elif No == 2:
        pass  # 列出学生姓名，选择要删除的学生名字
    elif No == 3:
        pass  # 列出学生姓名，选择要修改的学生名字
    elif No == 4:
        pass  # 输入要查询的学生信息。首先指定要查询的是名字还是其他信息
    else:
        print("输入有误，请重新输入")
