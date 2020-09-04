amount=[]
num=int(input())
average=0
for i in range(0,num):
    amount.append(float(input()))
    average+=amount[i]
average=average/num

e1=0
e2=0
for i in range(0,num):
    if(amount[i]<average):
        e1=average-amount[i]
    else:
        e2=amount[i]-average


if(e1<e2):
    print(e1)
else:
    print(e2)
