A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

last_A = V * T + A
last_B = W * T + B

print('YES' if last_A >= last_B else "NO")
