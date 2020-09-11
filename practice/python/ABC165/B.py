X = int(input())

money = 100
count = 0

while money < X:
  count += 1
  money = int(money * 1.01)

print(count)
