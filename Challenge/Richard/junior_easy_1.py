numbers = input("Enter six numbers seperated by a comma: ")
(number1, number2, number3, number4, number5, number6) = numbers.split(',')
number1 = int(number1)
number2 = int(number2)
number3 = int(number3)
number4 = int(number4)
number5 = int(number5)
number6 = int(number6)
point_shots_a = number1 * 3
point_shots_b = number4 * 3
field_goals_a = number2 * 2
field_goals_b = number5 * 2
free_throw_a = number3 * 1
free_throw_b = number6 * 1
total_a = point_shots_a + field_goals_a + free_throw_a
total_b = point_shots_b + field_goals_b + free_throw_b
if total_a > total_b:
    print('a')
elif total_a < total_b:
    print('b')
else:
    print('t')