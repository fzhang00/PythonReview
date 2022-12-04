f = open('junior_easy_2.txt', 'r')
line = f.readline() #number of lines of messages
lines_of_messages = int(line.strip('\n'))
list1 = []
for i in range(0, lines_of_messages):
    code = f.readline()
    code = code.strip('\n')  
    (number_part, character_part) = code.split(' ')
    number_part = int(number_part)
    decoded_message = (number_part * character_part + '\n')
    list1.append(decoded_message)

with open('decoded_message.txt', 'w') as f:
    f.writelines(list1)
# 1. use a variable to store the decoded message
# 2. create a empy list bofore the for loop
    # 2.1 append the decoded message into the empty list

# write to file
# use with statement like this
# with oepn("your next file name.txt",  'w') as f:
    # within the with block
    # loop throught the decoded meesage list
    # write each eleiemtn into the file. writeline()
