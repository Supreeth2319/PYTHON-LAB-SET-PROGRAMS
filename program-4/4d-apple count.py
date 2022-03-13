rcb = {'varun':{'apple':3,'mango':5},'supreeth':{'apple':10,'orange':6},'vikas':{'bannana':1,'apple':5}}
count = 0
for v in rcb.values():
    count += v.get('apple',0)
print(rcb)
print("The number of apples is", count)