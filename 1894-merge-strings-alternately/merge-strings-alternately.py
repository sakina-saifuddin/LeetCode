class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        mergedString=[]

        i=0

        while i<len(word1) or i < len(word2):

            if i<len(word1):
                mergedString.append(word1[i])

            if i < len(word2):
                mergedString.append(word2[i])

            i=i+1

        return "".join(mergedString)
        