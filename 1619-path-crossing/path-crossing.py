class Solution:
    def isPathCrossing(self, path: str) -> bool:

        x,y=0,0
        visit=set()

        visit.add((x,y))

        for char in path:
            if char=="N":
                y+=1
            elif char =="S":
                y-=1
            elif char =="E":
                x+=1
            else:
                x-=1
            
            if (x,y) in visit:
                return True
            visit.add((x,y))

        return False



        