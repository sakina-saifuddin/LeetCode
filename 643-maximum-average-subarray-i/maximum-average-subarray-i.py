class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:


        max_avg=0
        n=len(nums)
        curr_sum=0
        for i in range(k): #from i=0 till i=3 -> k=4-1 k=3
            curr_sum=curr_sum+nums[i]

        max_avg=curr_sum/k


        for i in range(k,n): #from k=4 (inclusive) to n=6 because n=7 but in range (k,n) the second value has -1 so i will be from i=4 till n=6
            curr_sum=curr_sum+nums[i]
            curr_sum=curr_sum-nums[i-k]
            curr_max_avg=curr_sum/k
            max_avg=max(max_avg, curr_max_avg)

        return max_avg








# nums=[1,2,3,4,5,6,7,8]
# k=4
# sol=Solution()
# max_avg_len=sol.findMaxAverage(nums, k)

# print("max_avg_len", max_avg_len)
        