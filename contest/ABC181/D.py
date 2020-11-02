from collections import Counter
S = input()
cnt = Counter(S)

if len(S) == 1:
  print('Yes' if S == '8' else 'No')
  exit()

if len(S) == 2:
  for i in range(16, 100, 8):
    if all(cnt[l] >= v for l,v in Counter(str(i)).items()):
      print('Yes')
      exit()
  else:
    print('No')
    exit()

for i in range(104, 1000, 8):
  if all(cnt[l] >= v for l,v in Counter(str(i)).items()):
    print('Yes')
    exit()
else:
  print("No")
