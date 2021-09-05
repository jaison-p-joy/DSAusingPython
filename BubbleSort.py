def bubbleSort(A,n):
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if(A[j] > A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
A = []
print("ENTER THE SIZE OF THE ARRAY: ")
n = int(input())
print("ENTER THE ARRAY: ")
for i in range(0,n):
    ele = int(input())
    A.append(ele)
bubbleSort(A,n)
print("SORTED ARRAY: ")
for i in range(0,n):
    print(A[i])

    