import string

N = int(input()) - 1
ss = string.ascii_lowercase

ans = ""

while N >= 0:
  ans += ss[N % 26]
  N = N // 26 - 1
  if N < 0:
    break

print(ans[::-1])
