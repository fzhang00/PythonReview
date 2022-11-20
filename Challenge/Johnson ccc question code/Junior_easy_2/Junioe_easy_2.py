l = open("decode_message.txt", "r")
l2 = int(l.readline().strip("\n"))
for i in range(l2):
    l3 = l.readline()
    if "\n" in l3:
        strip1 = l3.strip("\n")
    else:
        strip1 = l3
    l4 = strip1.split(" ")
    print(l4[1] * int(l4[0]))
