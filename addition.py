#Variables
x=7;
y=8;
print("sum of two numbers",x+y);
print("diff of two numbers",x-y);

a="vaibhav"
b="gupta"
msg=a+b;
print(msg);

x,y,z = "Vaibhav","Anushka","Vagmi"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Global Variable
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)