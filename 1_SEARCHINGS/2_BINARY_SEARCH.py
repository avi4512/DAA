from itertools import count
data =[-1,9,2,6,4,10]
data.sort()
x = int(input("Enter the number to Search:"))
low = 0
c = 0
high = len(data)-1
while low <= high:
    c = c + 1
    mid = (low + high) // 2
    if x == data[mid]:
        print(f"Found at {c}....")
        break
    else:
        if x > data[mid]:
            low = mid + 1
        else:
            high = mid - 1
else:
    print("Not Found...!")





