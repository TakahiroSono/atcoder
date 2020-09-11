S = input()
T = input()

st = [0] * (len(S) - len(T) + 1)

for i in range(len(S) - len(T) + 1):
  for j,t in enumerate(T):
    st[i] += S[i+j] == t

print(len(T) - max(st))
