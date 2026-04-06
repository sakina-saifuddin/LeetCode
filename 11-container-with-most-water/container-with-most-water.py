class Solution:
    def maxArea(self, height: List[int]) -> int:

        # maxarea=0
        # l=0
        # r=len(height)-1
        # i=0

        # while l < r:
        #     left=height[l]
        #     right=height[r]

        #     width=r-l
        #     hei=min(left, right)

        #     area=width*hei

        #     maxarea=max(maxarea,area)

        #     if left < right:
        #         l=l+1
        #     else:
        #         r=r-1

            
        
        # return maxarea
        #height.sort()
        maxarea=0
        l=0
        r=len(height)-1

        while l < r:
            left=height[l]
            right=height[r]

            width=(r-l)
            hei=min(left, right)

            area=width*hei

            maxarea=max(maxarea,area)

            if left < right:
                l=l+1
            else:
                r=r-1
            
        return maxarea


        