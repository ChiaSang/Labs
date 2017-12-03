import sys
# studentinfo = {}全局声明后在第一次写入数据i再次写入的会覆盖之前的数据，因为没有再次声明字典
studentName = []


def printStuName():
    for stuinfo in studentName:
        print(stuinfo['name'], end='\n')


print("学生管理系统 v0.1")
print("0退出系统")
print("1添加学生信息")
print("2删除学生信息")
print("3修改学生信息")
print("4查询学生信息")
print("5显示学生信息")
print("-" * 20)
while True:
    No = int(input("请选择功能\n"))
    if No == 0:
        print("退出")
        sys.exit()
    elif No == 1:  # 做一个循环，依次输入信息。判断每次输入的字符是不是exit，如果是则跳出循环
        studentinfo = {}
        stuid = input("请输入ID")
        stuname = input("请输入名字")
        stusex = input("请输入性别")
        stuage = input("请输入年龄")
        studentinfo['id'] = stuid
        studentinfo['name'] = stuname
        studentinfo['sex'] = stusex
        studentinfo['age'] = stuage
        studentName.append(studentinfo)
    elif No == 2:
        print("当前系统中存在的学生有\n")
        printStuName()
        for index1 in range(0, len(studentName)):
            print(index1)
        delname = int(input("请选择你要删除的学生姓名的编号\n"))
        del studentName[delname]
        # 列出学生姓名，选择要删除的学生名字
    elif No == 3:
        printStuName()  # 列出学生姓名，选择要修改的学生名字
        stuid1 = input("请输入要修改的ID")
        stuname1 = input("请输入要修改的名字")
        stusex1 = input("请输入要修改的性别")
        stuage1 = input("请输入要修改的年龄")
        studentinfo['id'] = stuid1
        studentinfo['name'] = stuname1
        studentinfo['sex'] = stusex1
        studentinfo['age'] = stuage1
    elif No == 4:
        selname = input(('请输入要查询的学生姓名：\n'))
        if selname in studentinfo:
            print(studentName.index(selname))
        else:
            print('对不起，数据不存在')
        pass  # 输入要查询的学生信息。首先指定要查询的是名字还是其他信息
    elif No == 5:
        print("*" * 10)
        printStuName()
        print("*" * 10)
    else:
        print("输入有误，请重新输入")
