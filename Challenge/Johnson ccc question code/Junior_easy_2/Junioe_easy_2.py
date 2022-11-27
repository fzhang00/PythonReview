dcode_msg_file = open("decode_message.txt", "r")
n_of_msg = int(dcode_msg_file.readline().strip("\n"))
dcoded_msg_lst = []
for i in range(n_of_msg):
    nextline = dcode_msg_file.readline()
    if "\n" in nextline:
        strip1 = nextline.strip("\n")
    else:
        strip1 = nextline
    split_dcode_msg = strip1.split(" ")
    dcoded_msg = split_dcode_msg[1] * int(split_dcode_msg[0])
    dcoded_msg_lst.append(dcoded_msg + "\n")
dcode_msg_file.close() 

with open("dcode_msg_looplist.txt", 'w') as f:
    for i in dcoded_msg:
        nfile = open("dcode_msg_looplist.txt", 'w')
        nfile.writelines(dcoded_msg_lst)