with open("c2.txt", "r") as f:
    lines = f.readlines()

a = lines[0]
b = lines[1]
c = lines[2]
d = lines[3]
e = lines[4]
if "\n" in a:
    a.strip('\n')
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)