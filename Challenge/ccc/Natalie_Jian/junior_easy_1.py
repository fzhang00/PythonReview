print(" ")
print("The Apples vs The Bananas basketball scores.")

print(" ")

app3 = int(input("Total number of 3-pointer shots from The Apples: "))
app2 = int(input("Total number of 2-pointer shots from The Apples: "))
app1 = int(input("Total number of 1-pointer shots from The Apples: "))
appTot = app3 * 3 + app2 * 2 + app1
print(" ")

if app3 and app2 and app1 <= 100:
    print(f"The total number of points from The Apples is {appTot}.")
elif app3 or app2 or app1 > 100:
    print("Error calculation")

print(" ")

ban3 = int(input("Total number of 3-pointer shots from The Bananas: "))
ban2 = int(input("Total number of 2-pointer shots from The Bananas: "))
ban1 = int(input("Total number of 1-pointer shots from The Bananas: "))
banTot = ban3 * 3 + ban2 * 2 + ban1
print(" ")

if ban3 and ban2 and ban1 <= 100:
    print(f"The total number of points from The Bananas is {banTot}.")
elif ban3 or ban2 or ban1 > 100:
    print("Error calculation")

banDiff = appTot - banTot
appDiff = banTot - appTot

print(" ")

if appTot > banTot:
    print(f"The Apples got {appTot} and beat The Bananas by {banDiff}, therefore the game result is A.")
    print(" ")
elif banTot > appTot:
    print(f"The Bananas got {banTot} and beat The Apples by {appDiff}, therefore the game result is B.")
    print(" ")
elif appTot == banTot:
    print(f"The Apples and The Bananas both got {appTot}, therefore the game result is T.")
    print(" ")
