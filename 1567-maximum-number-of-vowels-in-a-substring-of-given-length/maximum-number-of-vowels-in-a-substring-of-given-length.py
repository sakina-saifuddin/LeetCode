# class Solution:
#     def maxVowels(self, s: str, k: int) -> int:

#         maxcount=0
#         sub=""
#         for i in range(len(s)):
#             sub+=s[i]

#             if i >=k:
#                 sub=sub[1:] #remove left char in substring e.g sub="abci" after this line it will become "bci"

#             if i >=k-1:
#                 j=0
#                 count=0

#                 while j < len(sub):
#                     if sub[j] in "aeiou":
#                         count=count+1
#                     j=j+1
#                     maxcount=max(maxcount, count)

#         return maxcount
        

class Solution:
     def maxVowels(self, s: str, k: int) -> int:

        count=0
        maxcount=0
        for i in range(len(s)):
            if s[i] in "aeiou":
                count=count+1

            if i>=k:
                if s[i-k] in "aeiou":
                    count-=1
            if i>=k-1:
                maxcount=max(maxcount, count)

        return maxcount
        