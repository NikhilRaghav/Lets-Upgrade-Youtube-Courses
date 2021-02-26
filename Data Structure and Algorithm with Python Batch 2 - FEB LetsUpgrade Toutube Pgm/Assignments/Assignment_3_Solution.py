#Question 1
#Create an Array in python using the list and perform delete from any position operation

l=list(map(int,input().split()))
k=int(input("enter the position to be deleted"))
l.pop(k-1)

print("Numbers of list after removal ")
print(*l)
