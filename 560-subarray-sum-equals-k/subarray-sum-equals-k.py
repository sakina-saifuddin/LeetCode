class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefixsum=0
        prefixmap={0:1}
        count=0

        for i in range(len(nums)):
            prefixsum+=nums[i] #calculate sum

            earlierpart=prefixsum-k #remove the previous part as u move ahead
            if earlierpart in prefixmap:
                count+=prefixmap[earlierpart]
            prefixmap[prefixsum]=prefixmap.get(prefixsum, 0)+1      

        return count  