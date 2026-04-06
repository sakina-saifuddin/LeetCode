class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        r=0

        for l in range(1, len(nums)):
            if nums[l]!=nums[r]:
                r=r+1
                nums[r]=nums[l]

        return r+1
        