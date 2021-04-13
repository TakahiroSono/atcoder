r, x, y = map(int, input().split())

dist = (x**2 + y**2) ** 0.5

times = dist // r + bool(dist % r)

if dist // r == 0: times += 1
print(int(times))
