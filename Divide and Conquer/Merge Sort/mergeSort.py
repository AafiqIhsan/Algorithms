import merge

def mergeSortIter(A):
    p = 1
    length = len(A)
    while(p < length):
        for i in range(0,length,2*p):
            low = i
            mid = min(i+p-1, length-1)
            high = min(i +2*p-1, length-1)
            if(mid < high): merge.merge(A,low,mid,high)
        p*=2

def mergeSort(A,low,high):
    if(low >= high): return
    mid = (low+high)//2
    mergeSort(A,low,mid)
    mergeSort(A,mid+1,high)
    merge.merge(A,low,mid,high)

A = [8,5,2,1,7]
mergeSort(A,0,len(A)-1)

for elem in A:
    print(elem, end=" ")
