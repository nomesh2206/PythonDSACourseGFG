class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        ans = []

    	if (len(matrix) == 0):
    		return ans
    
    	m = r
    	n = c
    	seen = [[0 for i in range(n)] for j in range(m)]
    	dr = [0, 1, 0, -1]
    	dc = [1, 0, -1, 0]
    	x = 0
    	y = 0
    	di = 0
    
    	# Iterate from 0 to R * C - 1
    	for i in range(m * n):
    		ans.append(matrix[x][y])
    		seen[x][y] = True
    		cr = x + dr[di]
    		cc = y + dc[di]
    
    		if (0 <= cr and cr < m and 0 <= cc and cc < n and not(seen[cr][cc])):
    			x = cr
    			y = cc
    		else:
    			di = (di + 1) % 4
    			x += dr[di]
    			y += dc[di]
    	
    	return ans
