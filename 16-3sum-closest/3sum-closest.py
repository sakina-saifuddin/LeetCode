class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        closest=nums[0]+nums[1]+nums[2]

        for i in range(len(nums)-2): #making sapce for other two varaibles wherever the i is
                    l=i+1
                    r=len(nums)-1

                    while l<r:

                        currsum=nums[i] +nums[l]+nums[r]

                        if abs(currsum-target) < abs(closest-target):
                            closest=currsum
                        
                        if currsum<target:
                            l=l+1
                        elif currsum>target:
                            r=r-1
                        else:
                            return currsum

        return closest

        