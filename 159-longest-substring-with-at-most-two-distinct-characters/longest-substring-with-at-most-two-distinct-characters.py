class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        #s="hello"

        maxlen=0
        dicti={}
        l=0

        for r, char in enumerate(s):
            dicti[char]=dicti.get(char, 0) + 1 #add 'h' as key and its count as value so if 'h' not in dict count will be (0)+1 .get(char) -> gets the count for that char/key in the dict

            while len(dicti) > 2:  #if the length in the dictionary exceeds 2
                left_char=s[l]
                dicti[left_char]-=1

                if dicti[left_char]==0: #means only single count was there of that particular value then remove from dict
                    del dicti[left_char]
                l=l+1

            
            window=(r-l)+1

            maxlen=max(maxlen, window)

        return maxlen
                    


                


        