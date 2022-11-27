f = open('junior_easy_2.txt', 'r')
# First read the firs† line and get the number
line = f.readline()
n = line.strip("\n")
lines_of_messages = int(n)
# for lines of messages:
for i in range(0 ,lines_of_messages):
    # Reads next line
    line = f.readline()
    # Splits the space in between the number aand the symbol
    line1 = line.split(" ")
    # Number is the first part of the line
    number = line1[0]
    # Character is the second part of the line
    character = line1[1]
    # Strips the \n that is still in the character
    symbol = character.strip("\n")
    # Multiplies the symbol and the number and turns the number into a int then print it
    print(symbol * int(number))  
    # Strip the \n
    # Split by the space and get a list:  .split(" ")
    # Make the the symbol go how much times the number is
    # Save it and print it


# for numbers of egg:
    # print egg's color
