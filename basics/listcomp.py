num=[1,2,3,4,5,6]
# sq=[i*i for i in num]
# # for i in num:
# #     sq.append(i*i)
# print(sq)
# even=[i for i in num if i%2==0]
# print(even)
name=[" ali "," Tanay "]
cleaned_data=[i.strip().lower() for i in name if i]
print(cleaned_data)