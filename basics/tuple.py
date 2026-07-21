#tuple are also immutable unlike list
a=(1,2,3)
b=(1,)# always use , to create a single value tuple
# it has fewer methods like :
# count(),index(),len()
#Packing and unpacking
data = 10, 20, 30
a, b, c = data

#tuple canbe converted to list, it will create a new list ,existing tuple wont change
item=("hi",2,3)
lst=list(item)
print(type(item))
print(type(lst))
print(lst)