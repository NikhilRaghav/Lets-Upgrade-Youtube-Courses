'''
Question 1 :
Write a program to print the following pattern
1
22
333
4444
55555
'''
n=int(input("Enter n"))
for i in range(1,n):
  print(str(i)*i)

'''
Question 2 :
Write a Python program to add two numbers using class and object.
(Take both numbers as input from the user)
'''
class addition():
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def add_fun():
    return (self.a + self.b)
a=int(input("Enter first number"))
b=int(input("Enter second number"))

obj = addition(a,b)
print(obj.add_fun())
