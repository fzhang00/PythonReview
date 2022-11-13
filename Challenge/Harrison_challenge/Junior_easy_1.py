import random
shot_a3 = int(input("How many 3 point shots did The Apples make?"))
shot_a2 = int(input("How many 2 point shots did The Apples make?"))
shot_a1 = int(input("How many 1 point shots did The Apples make?"))
print(f"The Apples scored {shot_a3} 3-point shots, {shot_a2} 2-point shots and {shot_a1} 1-point shots")

shot_b3 = int(input("How many 3 point shots did The Bananas make?"))
shot_b2 = int(input("How many 2 point shots did The Bananas make?"))
shot_b1 = int(input("How many 1 point shots did The Bananas make?"))
print(f"The Bananas scored {shot_a3} 3-point shots, {shot_a2} 2-point shots and {shot_a1} 1-point shots")

total = shot_a3 * 3 + shot_a2 * 2 + shot_a1
print(f"The Apples got a grand score of {total}")

total2 = shot_b3 * 3 + shot_b2 * 2 + shot_b1
print(f"The Bananas got a grand score of {total2}")

if total > total2:
    print("The Apples have won the game!")
elif total < total2:
    print("The Bananas have won the game!")
elif total == total2:
    print("The game has been declared a tie!")

str
int
float