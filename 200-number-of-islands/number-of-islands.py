class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        totalrows=len(grid)
        totalcols=len(grid[0])
        island=0

        q=deque()
        visit=set() #to avoid duplicates, and handle our visited positions
        direction=[[0,1], [0,-1], [1,0], [-1,0]]

        def bfs(self, r, c): #so we will see the adjacent values of the current positon 
             q.append((r, c)) #q=[(0,0)]
             visit.add((r,c))

             while q:
                for _ in range(len(q)):
                    curr_r, curr_c=q.popleft()

                    for dr, dc in direction:
                        adj_r, adj_c=(dr+curr_r), (dc+curr_c)

                        if (adj_r, adj_c) not in visit and adj_r in range(totalrows) and adj_c in range(totalcols) and grid[adj_r][adj_c]=="1":
                            q.append((adj_r, adj_c))
                            visit.add((adj_r, adj_c))

        #iterate over the entire matrix

        for row in range(totalrows):
            for col in range(totalcols):
                if grid[row][col]=="1" and (row, col) not in visit:
                    bfs(self, row,col)
                    island+=1

        return island

        
        