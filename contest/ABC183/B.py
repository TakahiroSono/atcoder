sx, sy, gx, gy = map(int, input().split())

a = (gy + sy) / (gx - sx)
b = gy - a * gx

print(-b / a)
