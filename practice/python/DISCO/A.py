# 自力
# N = int(input())
# S = input()
# snow = S.count('-') - 1

# cnt = 0
# max_cnt = 0
# frozen_cnt = [0]
# st = 0

# frozen_num = [0] * N

# for i in range(1, N):
#   frozen_num[i] = frozen_num[i-1] + (1 / (i + 1))


# for n in range(N):
#   if S[n] == '>':
#     if not cnt:
#       st = n
#     cnt += 1
#   else:
#     if cnt:
#       frozen_cnt.append(cnt)
#     max_cnt = max(max_cnt, cnt)
#     cnt = 0

# ans = 0
# frag = True
# for fc in frozen_cnt:
#   if fc == max_cnt and frag:
#     frag = False
#     ans += frozen_num[fc+1]
#   else:
#     ans += frozen_num[fc]

# print(ans + snow)

# 解説参照
N = int(input())
S = input()

cnt = 0
max_cnt = 0
ans = 0
for n in range(N):
  if S[n] == '-':
    ans += 1
    cnt = 0
  else:
    ans += 1 / (cnt + 2)
    cnt += 1
    max_cnt = max(max_cnt, cnt)

print(ans - 1 + (1 / (max_cnt + 2)))
