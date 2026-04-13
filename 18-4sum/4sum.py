class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=set()
        numarr=nums
        n=len(numarr)


        for i in range(n):
            for j in range(i+1, n):
                left=j+1
                right=n-1

                while left<right:
                    summ=numarr[i]+numarr[j]+numarr[left]+numarr[right]

                    if summ==target:
                        res.add((numarr[i], numarr[j], numarr[left], numarr[right]))
                        left+=1
                        right-=1
                    elif summ<target:
                        left+=1
                    else:
                        right-=1

        return [list(x) for x in res]


      
        