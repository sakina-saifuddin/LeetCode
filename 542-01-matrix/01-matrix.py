class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        q=deque()

        rows=len(mat)
        cols=len(mat[0])        
        visit=set()
        direction=[[0,1],[0,-1],[1,0],[-1,0]]


        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==0:
                    visit.add((r,c))
                    q.append((r,c))

        while q:
            
            for _ in range(len(q)):
                curr_r, curr_c=q.popleft()

                for dr, dc in direction:
                    adjr, adjc=(dr+curr_r), (dc+curr_c)

                    if adjr>=0 and adjc>=0 and adjr in range(rows) and adjc in range(cols) and (adjr, adjc) not in visit and mat[adjr][adjc]==1:
                        mat[adjr][adjc]=mat[curr_r][curr_c]+1

                        visit.add((adjr, adjc))
                        q.append((adjr, adjc))


        return mat
                