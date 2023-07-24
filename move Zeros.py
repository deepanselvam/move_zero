def movezeros(ar, n):
    count = 0
    for i in range(n):
        if ar[i] != 0:
            ar[count] = ar[i]
            count += 1
    while count < n:
        ar[count] = 0
        count += 1
    return ar

n = int(input())
ar = list(map(int, input().split()))
ar1 = movezeros(ar, n)
print(ar1)
