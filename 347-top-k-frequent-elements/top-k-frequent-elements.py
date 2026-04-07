class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count={}
        result=[]
        freq=[[] for  _ in range(len(nums)+1)]

        for i in range(len(nums)):
            count[nums[i]]=count.get(nums[i], 0)+1

        for key, value in count.items():
            freq[value].append(key)

        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                
                if len(result)>=k:
                    break
                result.append(n)
                

        return result

        
        