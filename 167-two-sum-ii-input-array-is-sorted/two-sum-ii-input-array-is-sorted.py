class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l=0
        r=len(numbers)-1
        currsum=0

        for i in range(len(numbers)):

            while l<r:
                currsum=numbers[l]+numbers[r]

                if currsum < target:
                    l=l+1 #move left pointer to right
                elif currsum>target:
                    r=r-1 #move right pointer to left
                else:
                    return [l+1, r+1]