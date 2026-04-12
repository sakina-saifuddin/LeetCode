class Solution:
    def reorganizeString(self, s: str) -> str:

        count=Counter(s)

        maxheap=[(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(maxheap)

        result=[]
        reorganzied=""

        prevcount, prevchar=0, ""

        while maxheap:
            cnt, char=heapq.heappop(maxheap)
            result.append(char)

            if prevcount<0:
                heapq.heappush(maxheap, (prevcount, prevchar))

            cnt+=1
            prevcount, prevchar=cnt, char

        reorganzied="".join(result)

        return reorganzied if len(reorganzied)==len(s) else ""
        