data = [1,2,3,4,5]
x = int(input("Enter the value to search:"))
c = 0
for i in data:
    c = c + 1
    if x == i:
        print(f"Found at position {c}")
        break
else:
    print("Not Found")


