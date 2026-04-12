class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows=len(grid)
        cols=len(grid[0])
        island=0
        direction=[[1,0], [-1,0], [0,1], [0,-1]]

        def dfs(r,c):

            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=="0":
                return False

            grid[r][c]="0" 
            
            for dr, dc in direction:
                adjr, adjc=(dr+r), (dc+c)

                dfs(adjr, adjc)

                    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    dfs(r,c)
                    island+=1

        return island














        # totalrows=len(grid)
        # totalcols=len(grid[0])
        # island=0

        # q=deque()
        # visit=set() #to avoid duplicates, and handle our visited positions
        # direction=[[0,1], [0,-1], [1,0], [-1,0]]

        # def bfs(self, r, c): #so we will see the adjacent values of the current positon 
        #      q.append((r, c)) #q=[(0,0)]
        #      visit.add((r,c)) #we add psoition which is already seen
             

        #      while q:
        #         for _ in range(len(q)):
        #             curr_r, curr_c=q.popleft()

        #             for dr, dc in direction:
        #                 adj_r, adj_c=(dr+curr_r), (dc+curr_c)

        #                 if (adj_r, adj_c) not in visit and adj_r in range(totalrows) and adj_c in range(totalcols) and grid[adj_r][adj_c]=="1":
        #                     q.append((adj_r, adj_c))
        #                     visit.add((adj_r, adj_c))

        # #iterate over the entire matrix

        # for row in range(totalrows):
        #     for col in range(totalcols):
        #         if grid[row][col]=="1" and (row, col) not in visit:
        #             bfs(self, row,col)
        #             island+=1

        # return island

        
        