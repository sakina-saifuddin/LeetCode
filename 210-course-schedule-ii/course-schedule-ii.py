class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prereqmap={i:[] for i in range(numCourses)}
        listt=[]

        for crs, pre in prerequisites:
            prereqmap[crs].append(pre)

        visit=set()
        done=set()

        
        def dfs(crs):

            if crs in visit:
                return False
            
            # if prereqmap[crs]==[]:
            if crs  in done:
                return True

            visit.add(crs)

            for cr in prereqmap[crs]:

                if not dfs(cr):
                    return False
            visit.remove(crs)
            # prereqmap[crs]=[]
            done.add(crs)
            listt.append(crs)
            return True

        for cr in range(numCourses):
            if not dfs(cr):
                return []
        return listt 























        # graph={i:[] for i in range(numCourses)}

        # for i,j in prerequisites:
        #     graph[j].append(i)

        # state=[0]*numCourses #0->unvisited, 1-> visiting 2-> completed 

        # def dfs(course):

        #     if state[course]==1:
        #         return False
        #     if state[course]==2:
        #         return True

        #     state[course]=1 #currently visiting

        #     for nei in graph[course]:
        #         if not dfs(nei):
        #             return False

        #     state[course]=2
        #     return True

        # for i in range(numCourses):
        #     if not dfs(i):
        #         return False

        # return True

        # print(graph)
        
        