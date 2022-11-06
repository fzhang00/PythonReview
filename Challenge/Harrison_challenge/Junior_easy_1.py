import random
shot_a3 = (random.randint(0,100))
shot_a2 = (random.randint(0,100))
shot_a1= (random.randint(0,100))
print(shot_a3, shot_a2, shot_a1)

shot_b3 = (random.randint(0,100))
shot_b2 = (random.randint(0,100))
shot_b1= (random.randint(0,100))
print(shot_b3, shot_b2, shot_b1)

total = shot_a3 + shot_a2 + shot_a1
print(total)

total2 = shot_b3 + shot_b2 + shot_b1
print(total2)

if total > total2:
    print("The Apples have won the game!")
elif total < total2:
    print("The Bananas have won the game!")
elif total == total2:
    print("The game has been declared a tie!")
