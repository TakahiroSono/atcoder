from itertools import permutations

s1 = input()
s2 = input()
s3 = input()

s = set(list(s1) + list(s2) + list(s3))
if len(s) > 10:
  print("UNSOLVABLE")
  exit()

def trans(s1, s2, s3):
  for (s, i) in mask.items():
    s1 = s1.replace(s, i)
    s2 = s2.replace(s, i)
    s3 = s3.replace(s, i)
  return s1 ,s2, s3

def check(s1, s2, s3):
  return s1 + s2 == s3

mask = {}

for p in permutations(range(10), len(s)):
  for i,item in enumerate(s):
    mask[item] = str(p[i])
    re_s = trans(s1, s2, s3)
  for rs in re_s:
    if rs[0] == "0": break
  else:
    s1_num ,s2_num, s3_num = map(int, re_s)
    if check(s1_num ,s2_num, s3_num):
      print(s1_num ,s2_num, s3_num)
      exit()


print("UNSOLVABLE")
