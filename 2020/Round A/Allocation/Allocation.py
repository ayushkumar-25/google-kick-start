T = int(input())
for _ in range(T):
    sum = 0
    N, B = [int(x) for x in input().split()]
    l = list(map(int, input().split()))
    l.sort()
    for i in range(len(l)):
        try:
            if sum <= B:
                sum += l[i]
            if sum > B:
                break
        except Exception as e:
            pass
    print(f'Case #{_+1}: {i}')
