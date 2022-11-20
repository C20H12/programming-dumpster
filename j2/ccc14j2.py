votes = int(input())
voteStr = input()

aVotes = 0
bVotes = 0
for i in range(votes):
	if voteStr[i] == 'A':
		aVotes += 1
	else:
		bVotes += 1

if aVotes > bVotes:
	print("A")
elif bVotes > aVotes:
	print('B')
else:
	print("Tie")