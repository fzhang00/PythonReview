x = input("What would is your x?")
y = input("What would is your y?")
x=int(x)
y=int(y)
if (x<0) and (y<0):
    print("It's Quadrant 3.")
elif (x>0) and (y<0):
  print("It's Quadrant 4")
elif (x>0) and (y>0):
    print("It's Quadrant 1.")
elif (x<0) and (y>0):
  print("It's Quadrant 2.")