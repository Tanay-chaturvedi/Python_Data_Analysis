#sets are used to store multiple values in a variable where duplicate arent allowed
# st={1,5,6,1}
# print(st)# output={1,5,6} it will ignore extra 1

# ss=set() # a empty set named ss
# st.add("hi")
# print(st)
# st.update(["mnago","orange"])
# print(st)
# #in ouput of set you will get unique items but it does not takes care of order
# st.remove("mnago")
# print(st)
# st.pop() #it can remove anything
# print(st)
# st.clear()
# print(st) #output= set()

#operation in set
#union
a={1,2}
b={1,3,2}
print(a.union(b))
#intersection
print(a.intersection(b))