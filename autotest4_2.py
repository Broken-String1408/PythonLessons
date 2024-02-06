arr = [9, 15, 26, 11, 5, 3, 29, 33, 45, 51]

max1 = 0
for i in range(len(arr)):
    if  i != (len(arr) - 1):
        sum1 = arr[i - 1] + arr[i] + arr[i + 1]
        if sum1 > max1:
            max1 = sum1
            print(max1)
        i += 1
    else:
        sum1 = arr[i] + arr[i - 1] + arr[0]
        if sum1 > max1:
            max1 = sum1
            print(max1)
        i += 1    
print(max1)
