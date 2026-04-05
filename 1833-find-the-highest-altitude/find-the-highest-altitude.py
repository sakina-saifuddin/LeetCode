class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        n=len(gain)+1
        prefix=[0]*n
        prefix[0]=0
        
        for i in range(1,len(prefix)):
            prefix[i]=prefix[i-1] + gain[i-1]

        print(prefix)
        maxval=max(prefix)

        return maxval
        