N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
a_set = set(A)
b_set = set(B)
c_set = set(C)
a_dict = {a: 0 for a in a_set}
c_dict = {c: 0 for c in c_set}

for a in A:
  a_dict[a] += 1;

for c in C:
  c_dict[c] += 1;

ans = 0
for i,b in enumerate(B):
  if b in a_set and i+1 in c_set:
    ans += a_dict[b] * c_dict[i+1]

print(ans)
