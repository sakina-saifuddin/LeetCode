class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        #k=2

        maxlen=0
        l=0
        dicti={}

        for r, char in enumerate(s):
            dicti[char]=dicti.get(char, 0)+1  #adding char with tis count in the dict

        
        for key, values in dicti.items():
            if values < k:
                parts=s.split(key) #splitting teh string on bad character. e.g. if key=b, value=1 which means that value=1 < k=2
                #then we split the entire string on that character
                return max(self.longestSubstring(part, k) for part in parts)

          
            

        return len(s)



        