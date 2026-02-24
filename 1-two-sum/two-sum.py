class Solution(object):

    #sakina
    def twoSum(self, nums, target):
        print("hi")
        print(len(nums))
        indices=[]
    
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                 # j > i, no same element
                 if nums[i] + nums[j] == target:
                    indices.append(i)
                    indices.append(j)
                    return indices

        return indices

          
        print("indices", indices)
    
      
        
