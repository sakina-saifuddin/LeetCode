class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        #nums = [2,7,11,15]
        for i in range(len(nums)):

            complement=target-nums[i] #9-2 = 7 

            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]

            hashmap[complement]=i