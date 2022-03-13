a = input("Enter the string:")
b = a.split()
list(a)
while "the" in b:
    b.remove("the")
    c=" ".join(b)
print("After removing 'the' from a given string :",c)