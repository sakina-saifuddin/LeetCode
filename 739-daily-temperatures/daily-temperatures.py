class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        answer=[0]*len(temperatures)

        stack=[]

        for i in range(len(temperatures)):

            while stack and temperatures[i]>stack[-1][0]:
                oldtemp, oldindex=stack.pop()
                answer[oldindex]=i-oldindex

            stack.append((temperatures[i], i))



            if not stack:
                stack.append((temperatures[i], i))

        return answer
        