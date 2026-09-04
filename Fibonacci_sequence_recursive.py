def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
n=35 #To show the inefficiency of O(2^n) time complexity we can choose a larger value of n, but it will take a long time to compute.
for i in range(n+1):
    print(f"fibonacci({i}) = {fibonacci(i)}")