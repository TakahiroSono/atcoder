L, R, d = map(int, input().split())

ls = L // d
rs = R // d + (L % d == 0)

print(rs - ls)
