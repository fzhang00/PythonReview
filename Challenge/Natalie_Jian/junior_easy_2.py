with open("c2.txt", "r") as message1:
    line = message1.readline()

num_of_messages = int(line[0])

for i in range(num_of_messages):
    message1.readline()
    message2 = message2.strip("\n")
    message3 = message2.split(" ")
    whole_message = int(message3[0])*(message3[1])

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
    