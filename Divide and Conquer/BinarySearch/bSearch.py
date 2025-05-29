# Programmer: Dibbya Barua (Aafiq Ihsan)
# Date: May 28, 2025

def bSearch(L, key, low, high):
    if(low > high): return -1
    mid = (low + high) // 2
    if(key == L[mid]): return mid
    elif(key < L[mid]): return bSearch(L,key,low,mid-1)
    else: return bSearch(L,key,mid+1,high)

def bSearchIter(L, key, low, high):
    while(low <= high):
        mid = (low + high) // 2
        if(key == L[mid]): return mid
        elif(key < L[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return -1



list = [(3*(i**3) + 5*(i**2) + 2*(i) + 7) for i in range(10**5)]
val = 91642
key = 3*(val**3) + 5*(val**2) + 2*(val) + 7
index = bSearchIter(list, key, 0, len(list)-1)
print(index)