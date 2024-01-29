my_foods = ['pizza', 'falafel', 'carrot cake', 'biryani']
friend_foods = my_foods[1:2]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

for food in my_foods:
    print(f"{food.title()}, yum!")