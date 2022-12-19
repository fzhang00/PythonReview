
with open("c2.txt", "r") as f:
    line = f.readlines()

total_messages = int(line[0])
output_file = []

for i in range(1, total_messages+1):
    input = line[i].strip("\n")
    input_2 = input.split(" ")
    result = int(input_2[0])*(input_2[1])
    print(result)
    output_file.append(result + "\n")

with open("c2_output.txt", "w") as f:
    for i in output_file:
        final_result = open("c2_output.txt", "w")
        final_result.writelines(output_file)


# Repeat for n times using for loop
    # read a line
    # Strip the \n
    # seperate the symbol from the number
    # Decode the message using int
# print