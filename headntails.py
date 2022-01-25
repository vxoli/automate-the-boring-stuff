#Heads and Tails

import random

numberOfStreaks = 0

coinFlips = []
cumulativeMean = 0
numTrials = 0
while True:
	numberOfStreaks = 0
	for __ in range(10000):

		# Code that creates a list of 100 'heads' or 'tails' values.
		coinFlips = random.choices('HT', k=100)

		# Code that checks if there is a streak of 6 heads or tails in a row.
		numberOfStreaks += ('T'*6 in ''.join(coinFlips)) or ('H'*6 in ''.join(coinFlips))

	print('Chance of a streak = :%s%%' %(numberOfStreaks /100))
	cumulativeMean += numberOfStreaks / 100
	numTrials += 1
	print(cumulativeMean/numTrials)