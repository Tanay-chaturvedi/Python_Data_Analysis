# #Functions are used to group reusable code into a single block.
# They help make programs organized, readable, and easier to maintain.
# Instead of writing the same code again and again, you can define a function and reuse it whenever needed.



# def greet(name):
#     print("Hello",name)
# def add(a,b):
#     return a+b

# greet("tanay")
# print(add(2,3))

# def add(a,b):
#     return a+b
# c=add(4,6)
# print(c)


#using default parameter value
# def greet(name="broo"):
#     print("Hello", name)

# greet()
# greet("Harry")


#keyword argument
# def greet(name="yoo",city="delhi"):
#     print("hello",name,city)
# greet()
# greet(city="nimbahera",name="Tanay")


#lambda functions
# add=lambda a,b : print(a+b)
# add(2,3)

# add=lambda a,b: a+b
# print(add(4,5))


def calc(a, b):
    return a+b, a-b

# sum1 = calc(20,10)
# print(sum1)

sum1,diff=calc(20,10)
print(f"{sum1} and {diff}")