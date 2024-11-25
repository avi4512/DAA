data = [3,-1,8,1,0]
c = 0
x = len(data)
for i in range(x-1):
    for j in range(x-1):
        temp = data[j]
        c = c + 1
        if data[j] > data[j+1]:
            data[j] = data[j+1]
            data[j+1] = temp


        print(c,data)
