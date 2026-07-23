#A dictionary stores data in key : value pairs.
'''instead of :
name = "Tanay"
age = 22
city = "Bangalore"

we write:
'''
student = {
    "name": "Tanay",
    "age": 22,
    "city": "Bangalore"
}
# print(student)
# # print(student)
print(student["city"])

# # # can also create dictionary using dict()
# # st=dict(name="harry",age=22)
# # print(st)
# student["age"]=25
# print(student)

# #Methods
print(student.get("city"))
# # print(student.get("email"))#if key doesnt exists it gives None as output
# # student.pop("age")
# # print(student)
# #or use delete
# del student["age"]
# print(student)
# #insert a ket:value
# student["class"]=12
# print(student)

# #popitem() removes last inserted key
# student.popitem()
# print(student)
# print(len(student))#returns no. of key value pairs

# #loop through key
# for key in student:
#     print(key)
# #loop through values
# for val in student.values():
#     print(val)
# #through both
# for key, val in student.items():
#     print(key, val)
print(student.values())
print(student.keys())
print(student.items())
student.clear()#removes everyhting
