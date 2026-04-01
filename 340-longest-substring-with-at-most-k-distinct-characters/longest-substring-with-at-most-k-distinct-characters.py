class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        #s='hello
        #k=2

        maxlen=0
        l=0
        dicti={}

        for r, char in enumerate(s):
            dicti[char]=dicti.get(char, 0) +1


            while len(dicti) > k:
                left_char=s[l]
                dicti[left_char]-=1

                if dicti[left_char]==0:
                    del dicti[left_char]
                
                l=l+1

            maxlen=max(maxlen, (r-l)+1)

        return maxlen
        