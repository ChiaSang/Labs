Names = ["a.txt", "b.doc", "c.cpp", "d.rar", "e.jar", "f.exe"]
for tempname in Names:
    suffix = tempname.rfind(".")
    print(tempname[suffix:])
