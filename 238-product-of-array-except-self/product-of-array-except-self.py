class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n=len(nums)
        left=[1]*n
        right=[1]*n

        product=[1]*n

        #calculate everythig on the left of the ith value
        for i in range(1,len(nums)):
            left[i]=left[i-1]*nums[i-1]

        #calculate everythig on the left of the ith value
        for i in range(len(nums)-2, -1, -1):
            right[i]=right[i+1]*nums[i+1]

        print(left)
        print(right)

        
        for i in range(len(nums)):
            product[i]=left[i]*right[i]

        return product

        

































        # n=len(nums)
        # left=[1]*n
        # right=[1]*n
        # product=[1]*n
        # #building left array, everything except index 0
        # for i in range(1,n):
        #     left[i]=left[i-1] * nums[i-1]

        # for i in range(n-2,-1,-1):
        #     right[i]=right[i+1] * nums[i+1]

        # print(right)
        # print(left)
        # for i in range(n):
        #     product[i]=left[i]*right[i]

        # return product

        
        