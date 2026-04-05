class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        
        zeros=0
        maxcount=0
        l=0
        for r in range(len(nums)):
            if nums[r]==0:
                zeros=zeros+1

            while zeros > 1:
                if nums[l]==0:
                    zeros=zeros-1
                l=l+1

            maxcount=max(maxcount, (r-l) )  
        return maxcount
        