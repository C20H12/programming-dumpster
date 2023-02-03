def compute_kmp_failure(pattern):
  m = len(pattern)
  failure = [0] * m
  j = 0

  for i in range(1, m):
    while j > 0 and pattern[j] != pattern[i]:
      j = failure[j - 1]

    if pattern[j] == pattern[i]:
      j += 1

    failure[i] = j

  return failure


def kmp_search(text, pattern, failure):
  n = len(text)
  m = len(pattern)
  j = 0

  for i in range(n):
    while j > 0 and pattern[j] != text[i]:
      j = failure[j - 1]

    if pattern[j] == text[i]:
      j += 1

    if j == m:
      return True

  return False


text = input()
pattern = input()

l_text = len(text)
l_pattern = len(pattern)

failure = compute_kmp_failure(pattern)\

shifts = set([pattern[i:] + pattern[:i] for i in range(l_pattern)])

for i in range(l_text - l_pattern + 1):
  substr = text[i:l_pattern+i]
  if kmp_search(substr, shifts, failure):
    print("yes")
    break


print("no")