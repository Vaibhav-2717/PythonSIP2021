thislist = ["apple", "banana", "cherry"]
print(thislist);
thislist.insert(2,"Grapes");
print(thislist);

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist);
thislist.remove("banana")
print(thislist);

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist);

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist);