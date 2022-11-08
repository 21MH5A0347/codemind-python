a=int(input())
c=[]
for i in range(1,a):
    if a%i==0:
        c.append(i)
print(sum(c)==a)