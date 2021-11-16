def insertionSort(A):
    for i in range (1,len(A)):
        temp = A[i]
        j = i - 1
        while j >= 0 and A[j] > temp:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = temp

# driver code
A = [5, 4, 10, 1, 6, 2]
insertionSort(A) 
for i in range(len(A)):
    print(A[i])