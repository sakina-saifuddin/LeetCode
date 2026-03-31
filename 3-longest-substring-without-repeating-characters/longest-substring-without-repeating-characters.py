class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        w=0
        empset=set()
        r=0
        longest=0

        for i, char in enumerate(s):
            while char in empset:
                empset.remove(s[l])
                l=l+1

            empset.add(char)
            w=(r-l)+1
            r=r+1
            longest=max(longest, w)
        return longest





sol=Solution()

longestlen=sol.lengthOfLongestSubstring("hello")

print("longestlen", longestlen)
        