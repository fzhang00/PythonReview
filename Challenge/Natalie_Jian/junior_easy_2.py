with open("c2.txt", "r") as f:
    line = f.readlines()

num_of_messages = int(line[0])

for i in range(1, num_of_messages+1):
    input = line[i].strip("\n")
    line2 = input.split(" ")
    output = int(line2[0])*(line2[1])
    print(output)

for i in range(1, num_of_messages+1):
        output2 = line[i].strip("\n")
        output3 = output2.split(" ")
        output4 = int(output3[0])*(output3[1])
        written_output = list(output4)
        with open("c2_output.txt", "w") as f:
            f.writelines(written_output)

# with open("c2_output.txt", "w") as f:
#     f.writelines(written_output)

# with open("your output text file.txt", 'w' ) as f:
#     f.writelines(output_list)

# This the list you supplies to f.writelines()
# output_list = ['rgheos\n',  'osehgo\n', 'seothose']

# This is what you get in output.txt
# rgheos
# osehgo
# ....
# b1 = line[1]
# b_strip = b1.strip("\n")
# b_line = b_strip.split(" ")
# b = int(b_line[0])*(b_line[1])

    
# c1 = line[2]
# c_strip = c1.strip("\n")
# c_line = c_strip.split(" ")
# c = int(c_line[0])*(c_line[1])

# d1 = line[3]
# d_strip = d1.strip("\n")
# d_line = d_strip.split(" ")
# d = int(d_line[0])*(d_line[1])

# e1 = line[4]
# e_strip = e1.strip("\n")
# e_line = e_strip.split(" ")
# e = int(e_line[0])*(e_line[1])

# # decode the first line in the file to get number_of_message out of this line
# number_of_message = 5
# # repeat for number_of_message time by using for loop
# # for i in range(number_of_message):
#     # read another line, or reand the next element in your list
#     # strip
#     # split
#     # decoding

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
    