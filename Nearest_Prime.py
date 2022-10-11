for t in range(int(input())):
    n=int(input())
    next_prime=n+1
    while True:
        fc=0
        for i in range(1,next_prime +1):
            if next_prime%i==0:
                fc+=1
        if fc==2:
            break
        next_prime+=1
    pre_prime=n
    while True:
        fc=0
        for i in range(pre_prime,0,-1):
            if pre_prime%i==0:
                fc+=1
        if fc==2:
            break
        pre_prime-=1
    if n-pre_prime<=next_prime-n:
        print(pre_prime)
    else:
        print(next_prime)