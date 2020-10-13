S = input()

rain = {
  "SSS": 0,
  "SSR": 1,
  "SRS": 1,
  "SRR": 2,
  "RSS": 1,
  "RSR": 1,
  "RRS": 2,
  "RRR": 3
}

print(rain[S])
