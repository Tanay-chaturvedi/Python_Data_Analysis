#list can have multiple datatypes values
arr=[10,9,7]
print(arr.find(9))
# print(arr)
#list are mutable
# arr[0]=88
# print(arr)
# x=arr.pop()
# print(arr)
# del arr[1]
# print(arr)
# arr.clear()
# print(arr)
# print(2 in arr)
# a=[1,2]
# print(a*2)
# for i in a:
#     print(i)
# print(list(reversed(arr)))
# for i in range(3):
#     for j in range(2):
#         print(i, j)
# Multiplication table up to 5x5
for i in range(1, 6):   # rows
    for j in range(1, 6):  # columns
        print(i * j, end="\t")  # tab spacing
    print()  # new line after each row
