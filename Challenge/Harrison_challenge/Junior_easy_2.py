with open("C2.txt", "r") as f:
    line = f.readlines()

total_messages = int(line[0])

for i in range(1, total_messages+1):
    print(i)
    input = line[i].strip("\n") #line[i] grabs the value at index i
    input_b = input.split(" ")
    total = int(input_b[0])*(input_b[1])
    print(total)
    written_total = list(total[i])

with open("Output_C2.txt", "w") as f:
    f.writelines(written_total)


# Repeat for n times using for loop
    # read a line
    # Strip the \n
    # seperate the symbol from the number
    # Decode the message using int
# print