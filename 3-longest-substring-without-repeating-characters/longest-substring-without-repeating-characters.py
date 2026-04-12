class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxlen=0
        l,r=0,0
        sett=set()

        for i, char in enumerate(s):
            while char in sett:
                leftchar=s[l]
                sett.remove(leftchar)
                l+=1



            if char not in sett:
                sett.add(char)
                wind=(r-l)+1
                maxlen=max(maxlen, wind)
                r+=1

        return maxlen


















#         l=0
#         w=0
#         empset=set()
#         longest=0

#         for i, char in enumerate(s):
#             while char in empset:
#                 empset.remove(s[l])
#                 l=l+1

#             empset.add(char)
#             w=(i-l)+1
#             longest=max(longest, w)
#         return longest





# sol=Solution()

# longestlen=sol.lengthOfLongestSubstring("hello")

# print("longestlen", longestlen)
        

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:


#         l=0
#         max_len=0
#         empsett=set()

#         for r, char in enumerate(s):

#             while char in empsett:
#                 empsett.remove(s[l])

#                 l=l+1


#             empsett.add(char)
#             wind=(r-l)+1
#             max_len=max(max_len, wind)

#         return max_len
        

