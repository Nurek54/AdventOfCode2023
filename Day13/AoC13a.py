ll = open('AoC_Day13_Input.txt').read().strip().split('\n\n')

def transpose(x):
	return list(map(list, zip(*x)))

def findreflection(pattern, nonmatches):
	pattern = ["".join(x) for x in pattern]
	for i in range(len(pattern)-1):
		# reflect [0...i] to [i+1...len(pattern)-1]
		placesWhereDoesntWork = 0
		for j in range(len(pattern)):
			if i+1+(i-j) in range(len(pattern)) and pattern[j] != pattern[i+1+(i-j)]:
				placesWhereDoesntWork += len([k for k in range(len(pattern[j])) if pattern[j][k] != pattern[i+1+(i-j)][k]])
		if placesWhereDoesntWork == nonmatches:
			return i
	return None

def solve(pattern, nonmatches):
	pattern = [list(x) for x in pattern.split('\n')]
	row = findreflection(pattern, nonmatches)
	if row is not None:
		return 100*(row+1)
	col = findreflection(transpose(pattern), nonmatches)
	if col is not None:
		return (col+1)

p1 = 0

for i, l in enumerate(ll):
	p1 += solve(l, 0)

print("Part 1: ", p1)