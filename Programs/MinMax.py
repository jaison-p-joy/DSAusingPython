class MinMax: # a simple structure contains two variables min and max for storing min and max elements respectively
    def __init__(self):
        self.min = 0
        self.max = 0
    
def findMinMax(A: list, len: int) -> MinMax: #Function Annotation
    minmax = MinMax() #creating object
    if len == 1: #if the array contains only one element
        minmax.max = A[0]
        minmax.min = A[0]
        return minmax
    if A[0] > A[1]: #if the array contain two elements 
        minmax.max = A[0]
        minmax.min = A[1]
    else:
        minmax.max = A[1]
        minmax.min = A[0]
        
    for i in range(0, len):
        if A[i] > minmax.max:
            minmax.max = A[i]
        elif A[i] < minmax.min:
            minmax.min = A[i]
    return minmax 

if __name__ == "__main__":
    A = [0, 400, 6000, 70, 1, 3000]
    array_size = 6
    minmax = findMinMax(A, array_size) #passing array and its size also returns the object minmax 
    print("MAXIMUN ELEMENT IS : ", minmax.max)
    print("MINIMUM ELEMENT IS : ", minmax.min)
