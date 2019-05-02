def countchar(str):
    charmap = {}
    for i in range(26):
        charmap[chr(i + 65)] = 0
    str = str.upper()
    for c in str:
        if ord("A") <= ord(c) <= ord("Z"):
            charmap[c] += 1
        else:
            continue
    return[charmap[chr(i + 65)] for i in range(26)]


'''# countchar("abcdefghijklmnopqrstuvwxyz       ABCDEFGHIJKLMNOPQRSTUVWXYZ!
@#$%^&*()0987654321")'''


print(countchar('''abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()0987654321'''))
