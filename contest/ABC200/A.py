n = int(input())
cent = n // 100
cent += 1 if n % 100 else 0
print(cent)
