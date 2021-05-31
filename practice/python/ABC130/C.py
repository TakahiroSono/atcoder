W, H, x, y = map(int, input().split())

size = W * H / 2
line = 0
if x * 2 == W and y * 2 == H: line = 1

print(size, line)
