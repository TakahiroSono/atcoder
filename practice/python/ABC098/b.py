n = int(input())
s = input()

S = {}
for w in s:
  if w in S:
    S[w] += 1
  else:
    S[w] = 1

X = set([])
ans = 0
for w in s:
  X.add(w)
  S[w] -= 1
  if S[w] == 0: S.pop(w)
  cnt = 0
  for x in X:
    if x in S:
      cnt += 1
  ans = max(ans, cnt)

print(ans)
