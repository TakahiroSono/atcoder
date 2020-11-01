S = input()
eight = list(range(104, 1000, 8))
num = [0] * 10

if len(S) == 1:
  print('No' if int(S) % 8 else 'Yes')
  exit()

if len(S) == 2:
  print('Yes' if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0 else 'No')
  exit()

if len(S) == 3:
  for i in range(3):
    for j in range(3):
      if i == j: continue
      k = 0 if i != 0 and j != 0 else 1 if i != 1 and j != 1 else 2
      if int(S[i] + S[j]+ S[k]) % 8:
        continue
      else:
        print('Yes')
        exit()
  else:
    print('No')
    exit()

for i in range(10):
  num[i] = S.count(f'{i}')

for e in eight:
  se = str(e)
  for i in range(10):
    cnum = se.count(f'{i}')
    if cnum > num[i]:
      break
  else:
    print('Yes')
    exit()

print('No')
print('fin')
