S = input()
res = []
for i in range(4,len(S)):
  for j in range(len(S)-i):
    if sum(map(int, list(S[j:j+i+1]))) % 3 == 0 and int(S[j:j+i+1]) % 673 == 0:
      res.append((j+1,j+i+1))
print(len(res))
