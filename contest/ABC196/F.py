S = input()
T = input()

len_S = len(S)
len_T = len(T)

reans = 0

for i in range(len_S - len_T + 1):
  cnt = 0
  for s,t in zip(S[i:i+len_T], T):
    if s == t:
      cnt += 1
  reans = max(reans, cnt)

print(len_T - reans)






# T = input()

# len_S = len(S)
# len_T = len(T)

# if len_S == len_T:
#   cnt = len_S
#   for s, t in zip(S, T):
#     if s != t:
#       cnt -= 1
#   print(cnt)
#   exit()

# dp = [[0] * (len_S + 1) for _ in range(len_T + 1)]

# for i, t in enumerate(T, 1):
#   for j, s in enumerate(S, 1):
#     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#     if s == t:
#       dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)

# print(len_T - dp[-1][-1])

# for d in dp:
#   print(d)
