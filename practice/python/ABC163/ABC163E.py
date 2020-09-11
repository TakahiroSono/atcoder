def solve():
    INF = float('inf')

    def max2(x, y): return x if x >= y else y

    N = int(input())
    As = [(A, i) for i, A in enumerate(map(int, input().split()))]

    As.sort(reverse=True)

    dp = [[-INF]*(N+1) for _ in range(N+1)]
    dp[0][0] = 0
    for no, (A, pos) in enumerate(As):
        for i in range(no+1):
            j = no-i
            dp[i+1][j] = max2(dp[i+1][j], dp[i][j] + A*abs(pos-i))
            dp[i][j+1] = max2(dp[i][j+1], dp[i][j] + A*abs(pos-(N-1-j)))

    ans = 0
    for i in range(N+1):
        j = N-i
        ans = max2(ans, dp[i][j])

    print(ans)


solve()
