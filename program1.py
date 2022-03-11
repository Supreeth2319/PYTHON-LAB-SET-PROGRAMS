'''#1a to calculate sum of digits
n=int(input("Enter a number:"))
print("The number is",n)
sum=0
while(n>0 or sum>9):
    if(n==0):
        n=sum
        sum=0
    sum=sum+n%10
    n=n//10
print(f"sum of the {n} is {sum}")
if(sum==1):
    print("it is a magic number")
else:
    print("it is not a magic number")
'''

#1b printing all prime number less than particular number

n=int(input("Enter a number:"))
print("the prime numbers upto",n,"are")
for i in range(2,n):
    count=0
    for j in range(2,i):
            if(i%j==0):
                count+=1
    if(count==0):
            print(i)