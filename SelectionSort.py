A = []
print ("ENTER THE SIZE OF THE ARRAY: ")
n = int(input())
print ("ENTER THE ARRAY: ")
for i in range (0,n):
    ele = int(input())
    A.append(ele)
for i in range(n-1):
    iMin = i
    for j in range(i+1, n):
        if A[iMin] > A[j]:
            iMin = j
    A[i], A[iMin] = A[iMin], A[i]
print ("SORTED ARRAY: ")
for i in range(n):
    print(A[i])

        
        