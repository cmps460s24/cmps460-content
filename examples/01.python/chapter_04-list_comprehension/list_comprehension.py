# newlist = [espression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for s in fruits:
  if "a" in s:
    newlist.append(s)

print(newlist)

newlist2 = [s.title() for s in fruits if "a" in s]
print(newlist)


newlist = [s.upper() for s in fruits if s != "apple"]
print(newlist)

evens = [i ** 2 for i in range(10) if i % 2 == 0]
print(evens)