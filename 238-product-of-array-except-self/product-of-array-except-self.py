class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n=len(nums)
        left=[1]*n
        right=[1]*n
        product=[1]*n
        #building left array, everything except index 0
        for i in range(1,n):
            left[i]=left[i-1] * nums[i-1]

        for i in range(n-2,-1,-1):
            right[i]=right[i+1] * nums[i+1]

        for i in range(n):
            product[i]=left[i]*right[i]

        return product

        
        