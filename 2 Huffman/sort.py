def ascSort(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
                
ascSort(letterprob)
print("Ascending:"+str(letterprob))

def dscSort(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
                
dscSort(letterprob)
print("Descending:"+str(letterprob))
