#square
'''n=5
for i in range(n):
    for j in range(n):
        print('*',end=" ")
    print()'''
#print right angle triangle
'''n=5
for i in range(n):
    for j in range(i+1):
        print('*',end=" ")
    print()'''
#inverse of right angle triangle 
'''n=5
for i in range(n):
    for j in range(n-i):
        print('*',end=" ")
    print()'''
#diamiod pattern 
'''n=5
for i in range(n):
    for j in range(n-i-1):
        print("-",end="")
    for k in range(2*i+1):
        print("*",end=" ")
    print()
for i in range(n-2,-1,-1):
    for j in range(n-i-1):
        print("-",end=" ")
    for k in  range(2*i+1):
        print("*",end=" ")
    print()'''
#amstrong number
'''n=int(input("enter the number:"))
sum=0
lenght=len(str(n))
temp=n
while temp>0:
    digi=temp%10
    sum+=digi**lenght
    temp=temp//10
if n==sum:
    print("amstrong")
else:
    print("not amstrong")'''
# hallow square pattern
'''row=4
col=5
for i in range(row):
    for j in range(col):
        if i==0 or i==row-1 or j==0 or j==col-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
#pascal triangle
n=5
for i in range(n):
    for j in range(n-i-1):
        print("-",end="")
    for k in range(2*i+1):
        print(1+1,end=" ")
    print()