text = input()
pattern = input()

l_text = len(text)
l_pattern = len(pattern)

shifts = set([pattern[i:] + pattern[:i] for i in range(l_pattern)])
substrs = set([text[i:l_pattern+i] for i in range(l_text - l_pattern + 1)])

print("yes" if shifts & substrs else "no")
