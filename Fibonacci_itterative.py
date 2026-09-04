a, b = 0 ,1
n=100
for i in range(n+1):
    print(f"fibonacci({i})={a}")
    a, b = b, a + b