import array

def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)

def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp

def printArray(arr):
    for i in arr:
        print(i)

arr = array.array('i',[1,2,3,4,5])
leftRotate(arr, 2, len(arr))
printArray(arr)
