score = open('score.txt', 'r')
three_pointers_apples = int(score.readline()) * 3 #The readline() means to read the next line in the text file you added if you add an integer into the () it will read that many lines
two_pointers_apples = int(score.readline().strip('\n')) * 2 # The strip method is to get rid of the string inside the brackets
one_pointers_apples = int(score.readline().strip('\n'))

three_pointers_bananas = int(score.readline().strip('\n')) * 3
two_pointers_bananas  = int(score.readline().strip('\n')) * 2
one_pointers_bananas  = int(score.readline().strip('\n'))

apple_score = three_pointers_apples+two_pointers_apples+one_pointers_apples
banana_score = three_pointers_bananas+two_pointers_bananas+one_pointers_bananas

if apple_score > banana_score:
    print(f"Apples win with a score of {apple_score}")
elif apple_score == banana_score:
    print("Both team has the same amount of points, Tie game")
else:
    print(f"Bananas win with a score of {banana_score}")