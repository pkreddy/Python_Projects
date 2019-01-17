def BubbleSort(array):
    n = len(array)
    for i in range(n):
        
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                
arr = [12,1,13,11,15,16,2,2,5] 

BubbleSort(arr)
print(arr)
