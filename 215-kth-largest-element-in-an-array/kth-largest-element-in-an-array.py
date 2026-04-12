class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxheap=[]
        val=0

        for num in nums:
            heapq.heappush(maxheap, -num)

        for i in range(k):
            
            val=(-heapq.heappop(maxheap))

        return val

        print(nums)
        