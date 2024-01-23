def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1): # last i elements are already in place 
            for j in range(0,n-i-1):
                if arr[j] > arr[j+1]:
                    swap(arr, j, j+1)