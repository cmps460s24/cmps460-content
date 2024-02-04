student = (12345, 'Fatima', 'Saleh', 20)
print(f'Id: {student[0]} Fn: {student[1]}')
for sd in student:
    print(sd)

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    print(toppings)
    print(type(toppings))
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')