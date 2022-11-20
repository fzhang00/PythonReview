with open("c2.txt", "r") as f:
    lines = f.readlines()

a = lines[0]


b = lines[1]
b.strip("\n")
b.split(" ")
decrypted = int(b[0])*b[1]
print(decrypted)
    

    