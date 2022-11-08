def add(x):
    s=0
    while x>0:
        r=x%10
        s+=r
        x=x//10
    if s>9:
        return add(s)
    else:
        return s
a=int(input())
print(add(a))
        
        