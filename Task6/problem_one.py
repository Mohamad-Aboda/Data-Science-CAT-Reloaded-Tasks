n,b,d =  map(int,input().split())
sum = cnt = 0
a = list(map(int,input().split()))
 
for i in range(n):
    if(a[i]<=b):
        sum += a[i]
        if(sum > d):
            cnt+=1
            sum = 0
print(cnt)
