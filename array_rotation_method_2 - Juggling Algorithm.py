""" Juggling Algorithm. In this method, divide the array into M sets,
where M = GCD (n, d), and then rotate the elements in each set. From the
number of elements ( n ) of the array and number of rotations ( d ) to
be made to the array, the GCD(n, d) number of blocks are made. """

import array

def leftRotate(arr, d, n):
    d = d % n
    g_c_d = gcd(d, n)
    for i in range(g_c_d):
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

def printArray(arr):
    for i in arr:
        print(i)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

arr = array.array('i', [1, 2, 3, 4, 5, 6, 7])
d = 2
n = len(arr)

leftRotate(arr, d, n)
printArray(arr)
