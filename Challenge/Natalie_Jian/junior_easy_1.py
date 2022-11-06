print(" ")
print("The Apples vs The Bananas basketball scores.")

print(" ")

while True:
    app3 = int(input("Total number of 3-pointer shots from The Apples: "))
    if app3 > 100:
        print(" ")
        print("Error, points may not exceed 100.")
        print(" ")
        exit()
    app2 = int(input("Total number of 2-pointer shots from The Apples: "))
    if app2 > 100:
        print(" ")
        print("Error, points may not exceed 100.")
        print(" ")
        exit()
    app1 = int(input("Total number of 1-pointer shots from The Apples: "))
    if app1 > 100:
        print(" ")
        print("Error, points may not exceed 100.")
        print(" ")
        exit()
    appTot = app3 * 3 + app2 * 2 + app1
    print(" ")
    print(f"The total number of points from The Apples is {appTot}.")

    print(" ")

    ban3 = int(input("Total number of 3-pointer shots from The Bananas: "))
    if ban3 > 100:
        print(" ")
        print("Error, points may not exceed 100.")
        print(" ")
        exit()
    ban2 = int(input("Total number of 2-pointer shots from The Bananas: "))
    if ban2 > 100:
        print(" ")
        print("Error, points may not exceed 100.")
        print(" ")
        exit()
    ban1 = int(input("Total number of 1-pointer shots from The Bananas: "))
    if ban1 > 100:
        print(" ")
        print("Error, points may not exceed 100.")
        print(" ")
        exit()
    banTot = ban3 * 3 + ban2 * 2 + ban1
    print(" ")
    print(f"The total number of points from The Bananas is {banTot}.")

    print(" ")

    banDiff = appTot - banTot
    appDiff = banTot - appTot

    if appTot > banTot:
        print(f"The Apples got {appTot} and beat The Bananas by {banDiff}, therefore the game result is A.")
        print(" ")
        exit()
    elif banTot > appTot:
        print(f"The Bananas got {banTot} and beat The Apples by {appDiff}, therefore the game result is B.")
        print(" ")
        exit()
    elif appTot == banTot:
        print(f"The Apples and The Bananas both got {appTot}, therefore the game result is T.")
        print(" ")
        exit()