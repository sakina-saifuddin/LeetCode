class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        maxlen=0
        l=0
        dicti={}

        for r, char in enumerate(s):
            dicti[char]=dicti.get(char, 0)+1

        
        for key, values in dicti.items():
            if values < k:
                parts=s.split(key)
                return max(self.longestSubstring(part, k) for part in parts)

          
            

        return len(s)



        