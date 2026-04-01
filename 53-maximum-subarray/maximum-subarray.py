class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_sum=nums[0]
        maxsum=nums[0]


        for i in range(1, len(nums)):
            curr_sum=max(nums[i], curr_sum+nums[i])
            maxsum=max(maxsum, curr_sum)


        return maxsum

      