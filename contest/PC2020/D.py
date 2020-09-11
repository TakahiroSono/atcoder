N = int(input())
X = input()
cnt = X.count('1')
Y, Z = 0, 0
for i in range(N):
    if cnt > 1:
        Y = (Y + int(X[i])*pow(2, N-i-1, cnt-1))%(cnt-1)
    Z = (Z + int(X[i])*pow(2, N-i-1, cnt+1))%(cnt+1)

def popcount(n):
    c = bin(n).count('1')
    return c

for i in range(N):
    if X[i] == '1':
        pc = cnt - 1
        if pc <= 0:
            print(0)
            continue
        else:
            Y_i = (Y - pow(2, N-i-1, cnt-1))%(cnt-1)
            ans = 1
            while Y_i > 0:
                Y_i = Y_i % popcount(Y_i)
                ans += 1
            print(ans)
    else:
        Z_i = (Z + pow(2, N-i-1, cnt+1))%(cnt+1)
        ans = 1
        while Z_i > 0:
            Z_i = Z_i % popcount(Z_i)
            ans += 1
        print(ans)
