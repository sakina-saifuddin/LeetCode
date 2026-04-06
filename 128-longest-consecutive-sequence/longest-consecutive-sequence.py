class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset=set(nums)
        print(numset)
        longest=0

        for num in numset:
            if (num-1) not in numset: #e.g if first value is 100 then if 99 exists 
                length=1

                while (num+length) in numset:
                    length+=1

                longest=max( length, longest)
        return longest

        