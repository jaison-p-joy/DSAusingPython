#maxsum(Array (A), length of the array (n), no. of elements to pick (N))
#function sorts the array in decreasing order and then sums the first N numbers and returns the sum

def maxsum(A , n, N):
    maxSum = 0
    for i in range(0,n):
        for j in range(0, n-i-1):
            if(A[j] < A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
    for i in range(0,N-1):
        maxSum = maxSum + A[i]
    return maxSum
A = [5, -2, 3, 1, 2]
N = int(input('ENTER N : '))
Sum = maxsum(A, len(A), N)
print ('MAXINUM SUM IS : ',Sum)
