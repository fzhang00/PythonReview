f = open('junior_easy_2.txt', 'r')
# First read the firs† line and get the number
# f is a file object
line = f.readline()
n = line.strip("\n")
lines_of_messages = int(n)
# for lines of messages:
decoded_messages = []
for i in range(0 ,lines_of_messages):
    # Reads next line
    line = f.readline()
    # Splits the space in between the number aand the symbol
    line1 = line.split(" ") # TODO: what data type is line1? I think its a number
    # Number is the first part of the line
    number = line1[0] # TODO What is the method name (indexing ? slicing?) we used to pick element out of a sequence? I think it's slicing
    # Character is the second part of the line
    character = line1[1]
    # Strips the \n that is still in the character
    symbol = character.strip("\n")
    # Multiplies the symbol and the number and turns the number into a int then prints it
    #print(symbol * int(number))  
    # Strip the \n
    # Split by the space and get a list:  .split(" ")
    # Make the the symbol go how much times the number is
    # Save it and print it
    #---------------------------------
    # 1. use a variable to store the decoded message
    decoded_message = symbol * int(number) # TODO what does * do? It multiplies the symbol with the number
    # 2. create a empty list bofore the for loop

        # 2.1 append the decoded message into the empty list
    decoded_messages.append(decoded_message + "\n")
    print(decoded_messages)
# write to file
# use with statement like this
# with oepn("your next file name.txt",  'w') as f:
with open ("file.txt",'w') as f:
    # within the with block
    # loop through the decoded message list
       # print(decoded_message1)
        f.writelines(decoded_messages) 
    # write each element into the file. writelines()