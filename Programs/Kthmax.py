def sortArray(A, n):
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if(A[j] < A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
def kthMax(A, k):
    print(k,'th max', A[k-1])
A = [5, 6, 7, 4, 2, 3, 1]
sortArray(A,len(A))
print(A)
k = int(input())
kthMax(A, k)