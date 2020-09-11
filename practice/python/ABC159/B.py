S = input()
N = len(S)

def isPalindrome(s):
  n = len(s)
  re_s = s[::-1]
  for i in range(n // 2):
    if re_s[i] != s[i]:
      break
  else:
    return True
  return False

if isPalindrome(S) and isPalindrome(S[:N // 2]) and isPalindrome(S[(N + 1) // 2:]):
  print('Yes')
else:
  print('No')
