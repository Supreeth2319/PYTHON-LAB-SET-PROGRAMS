n = int(input("Enter the number:"))
def fib(n):
    a=[0]*n
    a[0]=0
    a[1]=1
    for i in range(2,n):
        a[i]=a[i-1]+a[i-2]
    print('The fibonicce is:')
    for i in range(0,n,1):
        print(a[i])
    print('The reverse order is:\n')
    for i in range(n-1,-1,-1):
        print(a[i])
fib(n)