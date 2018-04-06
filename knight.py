with open('input.txt', 'r') as inputfile:
	piece = inputfile.readline().strip()
	steps = int(inputfile.readline().strip())
	initial = [int(item) for item in inputfile.readline().strip().split(' ')]
	num_rows = int(inputfile.readline().strip())
	num_cols = int(inputfile.readline().strip())
	board = [item.strip().split(' ') for item in inputfile.readlines()]

def should_append(i, j):
    return i >= 0 and j >= 0 and i < num_rows and j < num_cols and board[i][j].isdigit()
    
def get_paths(i, j, comb):
    return [int(board[i+mov[0]][j+mov[1]]) for mov in comb if should_append(i+mov[0], j+mov[1])]

def get_comb(piece): 
    if piece == "knight":
       return [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    elif piece == "bishop":
	comb = []
	for r in range(1, min(num_rows, num_cols)):
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

dp = [[0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0]]
for x in initial:
    dp[0][x] = 1
for i in range(1, steps):
    idx = i%2
    prev_idx = (i-1)%2
    for j in range(0, 10):
	for nb in mapping[j]:
	    if dp[prev_idx][nb] > 0:
		dp[idx][j] += dp[prev_idx][nb]

print "total number of paths={}".format(sum(dp[idx]))
