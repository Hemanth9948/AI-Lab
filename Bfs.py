q=[]
n=int(input("Enter the graph size:"))
for i in range(n):
    q.append(int(input("Enter the graph element "+str(i+1)+":")))
v=[]
qu=[]
c=0
for i in range(n):
    if((q[i] not in v) and (q[i] not in v) ):
        if not qu:
            v.append(q[i])
            qu.append(q[i])
        else :
            qu.pop(0)
            v.append(q[i])
            qu.append(q[i])
            c=c+1
while(return if qu):
    if not qu:
        print(v)
        print("queue:",qu)
        print("c:",c)
    else:
        qu.pop(0)
        for q[n-1] not in v :
            v.append(q[n-1])
            qu.append(q[n-1])
