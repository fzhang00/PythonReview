with open("c2.txt", "r") as f:
    line = f.readlines()

num_of_messages = int(line[0])
output_file = []

for i in range(1, num_of_messages+1):
    input = line[i].strip("\n")
    line2 = input.split(" ")
    output = int(line2[0])*(line2[1])
    print(output)
    output_file.append(output + "\n")

with open("c2_output.txt", "w") as f:
    f.writelines(output_file)
