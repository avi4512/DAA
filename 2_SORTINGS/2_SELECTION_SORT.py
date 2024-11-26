a = [3,8,10,4,2,1]
n = len(a)
c = -1
for i in range(n):
    min = i
    c = c + 1
    for j in range(i+1,n):
        if a[min] > a[j]:
            min = j
    if min != i:
        a[min],a[i] = a[i],a[min]

    print(c,a)
