class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        totalrows=len(grid) #total no of rows
        totalcols=len(grid[0]) #total no of columns
        q=deque() #create empty queue to hold alll the rotten oranges

        fresh, time =0,0

        for r in range(totalrows):
            for c in range(totalcols):
                if grid[r][c]==1:
                    fresh+=1 #calculating the no of fresh oranges
                if grid[r][c]==2:
                    q.append([r,c]) #adding the position of the rotten oranges in the queue
        
        direction=[[0,1],[0, -1], [1,0], [-1, 0] ]
        while q and fresh >0: #xecute till q has some values
            
            

            for _ in range(len(q)):
                rotten_r,rotten_c=q.popleft() #take the first rotten out of the queuue, now we will make all the adjacent fresh oranges from this positon to rotten aswell
                for dr, dc in direction:
                    fresh_r, fresh_c=(dr+rotten_r), (dc+rotten_c) #find psoiton of fresh to make it rotten now
                    
                    if fresh_r <0 or fresh_r==totalrows or fresh_c<0 or fresh_c==totalcols or grid[fresh_r][fresh_c]!=1:
                        continue
                        
                    
                    grid[fresh_r][fresh_c]=2
                    fresh-=1 #now the ornage in the fresh_r and fresh_c position is not fresh anymore so we reduce the count
                    q.append([fresh_r, fresh_c])

            time+=1 #once the orange present in q adjacent oranges are turn rotten increase time by 1

        return time if fresh==0 else -1 #we return the actual time if we converted all the fresh into rotten, and -1 if still any fresh orange is left in the orange



        