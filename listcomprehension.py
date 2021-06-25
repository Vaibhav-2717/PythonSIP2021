fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist);


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist);

newlist = [x for x in fruits if x != "apple"];

newlist = [x for x in range(10) if x < 5];

newlist = [x if x != "banana" else "orange" for x in fruits];