class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph={i:[] for i in range(numCourses)}

        for i,j in prerequisites:
            graph[j].append(i)

        state=[0]*numCourses #0->unvisited, 1-> visiting 2-> completed 

        def dfs(course):

            if state[course]==1:
                return False
            if state[course]==2:
                return True

            state[course]=1 #currently visiting

            for nei in graph[course]:
                if not dfs(nei):
                    return False

            state[course]=2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

        print(graph)
        