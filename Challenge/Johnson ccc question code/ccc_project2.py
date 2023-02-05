x = input("What is your x coordinate?:")
y = input("What is your y coordinate?:")
if int(x) > -1 and int(y) > -1:
    print("Quadrant 1")
elif int(x) < 0 and int(y) > -1:
    print("Quadrant 2")
elif int(x) < 0 and int(y) < 0:
    print("Quadrant 3")
elif int(x) > -1 and int(y) < 0:
    print("Quadrant 4")
else:
    print("Error")
