arr = [12, 3, 10, 1, 2, 15, 10, 1, 8]
n = len(arr)

for i in range(1, n):
    value = arr[i]
    hole = i
    while (hole>0 and arr[hole-1]>value):
        arr[hole] = arr[hole-1]
        hole = hole - 1
    arr[hole] = value

print(arr)
    
