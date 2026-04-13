class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxfruits=0
        baskets=2
        left=0
        fruitstype={}

        for i in range(len(fruits)):
            fruitstype[fruits[i]] = fruitstype.get(fruits[i], 0) + 1

            while len(fruitstype)>baskets:
                fruitstype[fruits[left]]-=1

                if fruitstype[fruits[left]]==0:
                    del fruitstype[fruits[left]]

                left+=1
                
            maxfruits=max(maxfruits, (i-left)+1)

        return maxfruits

         

 