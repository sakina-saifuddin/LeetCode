class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left=0
        right=len(nums)-1

        while left<=right:
            mid=(left+right)//2

            if nums[mid]==target:
                return mid

            #left sorted half
            
            if nums[left]<=nums[mid]:
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1

            else:
                if nums[mid]< target <=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1

                


        

        # l=0
        # r=len(nums)-1

        # mid=(l+r)//2

        # while l<=r:
        #     if target not in nums:
        #         return -1

        #     if nums[r]==target:
        #         return r
        #     elif nums[l]==target:
        #         return l
        #     elif nums[l]>target:
        #         l+=1
        #     else:
        #         r-=1

        


       