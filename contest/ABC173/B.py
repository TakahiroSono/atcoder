N = int(input())


judge = { j: 0 for j in ['AC', 'WA', 'TLE', 'RE' ]}

for i in range(N):
  j = input()
  judge[j] += 1

for (j, n) in judge.items():
  print(j, 'x', n)
