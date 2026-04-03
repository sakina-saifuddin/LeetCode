class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:


        result=[]
        withextra=0
        max_val=candies[0]
        newarr=[]

        for i in range(len(candies)):
            withextra=candies[i]+extraCandies
            newarr.append(withextra)
            if candies[i] > max_val:
                max_val=candies[i]

        for i in range(len(newarr)):
            if newarr[i]>=max_val:
                result.append(True)
            else:
                result.append(False)

        return result


        