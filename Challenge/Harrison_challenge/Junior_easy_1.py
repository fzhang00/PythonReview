import random
shot_a3 = (random.randint(0,100))
shot_a2 = (random.randint(0,100))
shot_a1= (random.randint(0,100))
print(f"The Apples scored {shot_a3} 3-point shots, {shot_a2} 2-point shots and {shot_a1} 1-point shots")

shot_b3 = (random.randint(0,100))
shot_b2 = (random.randint(0,100))
shot_b1= (random.randint(0,100))
print(f"The Bananas scored {shot_a3} 3-point shots, {shot_a2} 2-point shots and {shot_a1} 1-point shots")

total = shot_a3*3 + shot_a2*2 + shot_a1
print(f"The Apples got a grand score of {total}")

total2 = shot_b3*3 + shot_b2*2 + shot_b1
print(f"The Bananas got a grand score of {total2}")

if total > total2:
    print("The Apples have won the game!")
elif total < total2:
    print("The Bananas have won the game!")
elif total == total2:
    print("The game has been declared a tie!")
