#Problem: Given an array A consisting of N integers, return the array after rotating it to the right by k steps.
A = [3, 4, 5, 6, 7, 8, 9, 13, 45, 67, 20]
k=3
def shift(A):
    N = len(A)
    results = []
    for i in range(N):
        target = (i-k) % N
        results. append(A[target])
    return results    
print(f"Shifted array: {shift(A)}")