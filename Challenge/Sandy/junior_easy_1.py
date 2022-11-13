apples3 = input("How much 3 points apples scored")
apples2 = input("How much 2 points apples scored")
apples1 = input("How much 1 points apples scored")
apples_score = int(apples3)*3 + int(apples2)*2 + int(apples1)*1
print(apples_score)

banana3 = input("How much 3 points banana scored")
banana2 = input("How much 2 points banana scored")
banana1 = input("How much 1 points banana scored")
banana_score = int(banana3)*3 + int(banana2)*2 + int(banana1)*1
print(banana_score)

if apples_score > banana_score:
    print('The Apples won!')
elif banana_score > apples_score:
    print('The Bananas won!')   
else:
    print('It was a tie.')