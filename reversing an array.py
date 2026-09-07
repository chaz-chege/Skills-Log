#The question is: Given array A consisting of N integers, return the reversed array.
A = [1, 2, 3, 4, 5]
def reverse_array(A):
    N = len(A)
    for i in range(N//2):
        A[i], A[N-i-1] = A[N-i-1], A[i]
    return A

print(f"Reversed array: {reverse_array(A)}") # Output: [5, 4, 3, 2, 1]
