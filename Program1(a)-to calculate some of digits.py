n=int(input("Enter a number:"))
print("The number is",n)
sum=0
while(n>0 or sum>9):
    if(n==0):
        n=sum
        sum=0
    sum=sum+n%10
    n=n//10
print(f"sum of the digits is:", sum)
if(sum==1):
    print("it is a magic number")
else:
    print("It is not a magic number")
