# 三种方法取出字符d
a = "abcd"
b = a[3]
c = a[(len(a) - 1)]
e = a[3:]
f = len(a)
print(b)
print(c)
print(e)
print(f)
#------------------字符串的拼接------------------------------
x = "jay"
y = "python"
w = y.replace("p", "rr")  # 一种替换的方法
# z = x + y 最不好的一种字符串的拼接方法，不推荐
print("My name is %s , i love %s" % ("zk", 'python'))  # 注意占位符的语法格式
g = "".join([x, y])
print(w)
print(g)
#-----------------练习题--------------------------
