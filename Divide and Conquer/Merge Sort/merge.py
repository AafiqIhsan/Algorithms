# Programmer: Aafiq Ihsan (Dibbya Barua)
# Date: May 28 ,2025
# This file defines a merge function that takes input
# an array A, and the indices low, mid, and high, and
# merges the sub-arrays into one sorted array

def merge(A,low,mid,high):
    C = []
    i,j = low,mid+1

    while (i <= mid and j <= high):
        if(A[i] < A[j]):
            C.append(A[i])
            i += 1
        else:
            C.append(A[j])
            j += 1
    for elem in A[i:mid+1]:
        C.append(elem)
    for elem in A[j:high+1]:
        C.append(elem)
    
    for k in range(len(C)):
        A[low+k] = C[k]