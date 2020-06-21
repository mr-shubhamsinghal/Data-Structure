arr = [7, 5, 4, 2, 3, 1]
n = len(arr)

for i in range(1, n):
    num = arr[i]
    hole = i
    while hole > 0 and arr[hole-1] > num:
        arr[hole] = arr[hole-1]
        hole -= 1
    arr[hole] = num
print(arr)
