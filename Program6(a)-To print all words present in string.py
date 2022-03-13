n = input("Ente a string:")
a = n.split()
for i in a:
    print('The word ',i,' has ',len(i),' character')
print('The total number of words are',len(a))
