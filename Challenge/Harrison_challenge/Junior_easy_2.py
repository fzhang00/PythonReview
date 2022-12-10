with open("C2.txt", "r") as f:
    line = f.readline()

total_messages = int(line[0])

for i in range(1, total_messages):
    input_a = line
    input_b = input_a.strip("\n")
    input_c = input_b.split(" ")
    total = int(input_c[0])*(input_c[1])


# Repeat for n times using for loop
    # read a line
    # Strip the \n
    # seperate the symbol from the number
    # Decode the message using int
# print