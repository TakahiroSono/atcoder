N, M = map(int, input().split())

odd = (M * (M - 1)) / 2
even = (N * (N - 1)) / 2

print(int(odd + even))
