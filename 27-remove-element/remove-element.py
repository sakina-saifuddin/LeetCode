class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k=0

        for num in nums:

            if num!=val:
                nums[k]=num
                k+=1
            
        # while k < len(nums):
        #     nums[k]=-1

        return k

               

        