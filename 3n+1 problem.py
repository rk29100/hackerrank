n= int(input("enter a number"))
c=1
while n!=1:
    if n%2==0:
       n=n/2
       c+=1
    else:
        n=3*n+1
        c+=1
    
print(c)
