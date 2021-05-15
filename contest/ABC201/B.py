n = int(input())

mt = []
for i in range(n):
  name, h = input().split()
  mt.append((int(h), name))

mt.sort()
print(mt[-2][1])
