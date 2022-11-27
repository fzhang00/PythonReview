f = open('junior_easy_2.txt', 'r')
line = f.readline() #number of lines of messages
lines_of_messages = int(line.strip('\n'))
for i in lines_of_messages:
    f.readline()
    code = line.strip('\n')
    (number_part, character_part) = code.split(' ')
    number_part = int(number_part)
    print(number_part * character_part)