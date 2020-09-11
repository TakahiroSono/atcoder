A, B = input().split()
A = int(A)
Bc, Bp = map(int, B.split("."))
print(A*Bc + A*Bp//100)
