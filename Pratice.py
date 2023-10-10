
#                                                 ------------------------------ Factorial ------------------------------
"""
n=eval(input("enter the number :"))
f=1
if(n==0 or n<0):
    print("Enter the Correct Value (which is >0)")
else:
    for i in range(1,n+1):
	    f=f*i;
    print("factorial of the given number is ",f)
"""


#                                                 ------------------------------ FibanocciSeries ------------------------------
"""                                                 
n=int(input("Enter the Number:"))
l=[0,1]
if(n==0):
    print("Fibanocci series is ",l[0])
elif(n==1):
        print("Fibanocci series is ",l)
else:
    for i in range(2,n):
	    f=l[i-1]+l[i-2]
	    l.insert(i,f)
    print("Fibanocci series is ",l)
"""

#                                                 ------------------------------ Armstrong Number ------------------------------
"""
n=int(input("Enter the Number:"))
t=n
j=s=0
m=str(n)
for i in m:
	j=j+1
while(n%10!=0):
    temp=int(n%10)
    a=pow(temp,j)
    s=s+a
    n=n/10
if(t==s):
    print("The given number is Armstrong Number")
else:
    print("The given number is  Not  Armstrong Number")
"""
#                                                 ------------------------------ PrimeNumber ------------------------------

n=int(input("Enter the Number:"))
c=0
for i in range(1,n):
	if(n%i==0):
		c=c+1
if(c==1):
	print("The given number is PrimeNumber")
else:
	print("The given number is Not PrimeNumber")
