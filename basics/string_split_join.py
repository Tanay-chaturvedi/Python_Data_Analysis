#strings are immutable
# slicing string[start:end]
# name="Tanay"
# print(name[:])

# print(name[::2]) #prints every 2nd charcter
# print(name[::-1])#reverse
# print(len(name))
# name = "  Tanay  "
# print(name)
# print(name.strip())
# a=name.strip()
# print(a.replace("T","Q"))
# print(name.find("T"))
# text = "apple,banana,orange"
# print(text.split())
# print(text.split(","))
# items = text.split(",")
# print(items)
# a="hi"
# b="yo"
# print(a+" "+b)
words = ["Python", "is", "awesome"]

print(" ".join(words))
print(",".join(words))
print(" | ".join(words))