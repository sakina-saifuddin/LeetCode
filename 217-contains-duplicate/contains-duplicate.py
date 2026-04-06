class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashmap={}
        num=2
        distinctFound=False


        for  i in range(len(nums)):
            hashmap[nums[i]]=hashmap.get(nums[i], 0)+1

        
        for key in hashmap:
            if hashmap[key] > 1:
                return True
        
                
                
        return False

       
                

        print("fdf", hashmap)

      
            

        
        