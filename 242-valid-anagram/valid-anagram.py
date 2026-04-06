class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        anaghashs={}
        anaghasht={}

        for i, char in enumerate(s):
            anaghashs[char]=anaghashs.get(char,0)+1

        for i, char in enumerate(t):
            anaghasht[char]=anaghasht.get(char,0)+1

        if anaghashs==anaghasht:
            return True
        else:
            return False

        