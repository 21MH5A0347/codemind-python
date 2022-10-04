
n = int(input())
for i  in range (n):
    a,b = map(int,input().split())
    s = input()
    lst = s[b:]
    s=s[:b]
    r=""
    for i in range(len(s)//2):
        r+=s[i]
        r+=s[-(i+1)]
        
    if len(s)%2:
        r+=s[len(s)//2]
    r=r[::-1]
    print(r+lst)