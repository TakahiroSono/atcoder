for i in range(10):
  print(i)
  if i > 5:
    break
else:
  print("i < 4")

x = 0
for i in range(x):
  print(i)
  if i > 5:
    break
else:
  print("i < 4")

for i in range(5):
  print(i)
  if i > 5:
    exit()

print("i < 4")
