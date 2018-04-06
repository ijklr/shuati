with open('input.txt', 'r') as inputfile:
	piece = inputfile.readline().strip()
	steps = int(inputfile.readline().strip())
	initial = [int(item) for item in inputfile.readline().strip().split(' ')]
	num_rows = int(inputfile.readline().strip())
	num_cols = int(inputfile.readline().strip())
	board = [item.strip().split(' ') for item in inputfile.readlines()]

def should_append(ii, jj):
    return ii >= 0 and jj >= 0 and ii < num_rows and jj < num_cols and board[ii][jj].isdigit()
    
def get_paths(i, j, comb):
    return [board[i+mov[0]][j+mov[1]] for mov in comb if should_append(i+mov[0], j+mov[1])]

def get_comb(piece): 
    if piece == "knight":
       return [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    elif piece == "bishop":
	comb = []
	for r in range(1, min(int(num_rows), int(num_cols))):
	    comb += [(r, r), (r, -r), (-r, r), (-r, -r)]
	return comb
    else:
	return []

mapping = {}
for i in range(len(board)):
    for j in range(len(board[i])):
	comb = get_comb(piece)
	val = board[i][j]
	if val.isdigit():
	    mapping[int(val)] = get_paths(i, j, comb)

print "piece={}, mapping={}".format(piece, mapping) 

dp = [[0 for col in range(10)] for row in range(steps)]
for x in initial:
    dp[0][x] = 1
for i in range(1, steps):
    for j in range(0, 10):
	if dp[i-1][j] > 0:
	    dp[i][j] = len(mapping[j]) * dp[i-1][j]

print "dp={}".format(dp)
print "total number of paths={}".format(sum(dp[-1]))
