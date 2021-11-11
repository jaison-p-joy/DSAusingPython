def reverseArray(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start] #swapping the elements
        start += 1
        end -= 1
A = [1, 2, 3, 4, 5, 6] #array
print(A)
reverseArray(A, 0, 5) #passing array, starting index, ending index
print("REVERSED ARRAY")
print(A)    