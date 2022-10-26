h,m=list(map(int,input().split(':')))
x=abs((30*h)-(11*m/2))
print(min(x,360-x))