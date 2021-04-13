N = input()

if N == "0":
  print('Yes')
  exit()

while 1:
  if N[-1] == "0": N = N[:-1]
  else: break

for i in range(len(N)):
  if N[i] == N[-i-1]: continue
  break
else:
  print("Yes")
  exit()

print('No')
