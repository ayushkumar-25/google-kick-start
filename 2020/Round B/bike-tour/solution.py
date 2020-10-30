t = int(input())
for i in range(t):
    count = 0
    n = int(input())
    l = list(map(int, input().split()))
    for j in range(1,len(l)-1):
        if l[j-1]<l[j] and l[j+1]<l[j]:
            count += 1
        
    print(f'Case #{i+1}: {count}')