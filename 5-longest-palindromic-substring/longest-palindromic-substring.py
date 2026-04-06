class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen=0
        l=0
        r=0
        palin=""

        for i in range(len(s)):
            
            #for odd length
            l=i
            r=i

            while l>=0 and r<len(s) and s[l]==s[r]:

                reslen=(r-l)+1
                
                if reslen>maxlen:
                    palin=s[l:r+1]
                    maxlen=reslen
                
                l=l-1
                r=r+1

            #for even len

            l=i
            r=i+1
            while l>=0 and r < len(s) and s[l]==s[r]:

                reslen=(r-l)+1
                if reslen > maxlen:
                    palin=s[l:r+1]
                    maxlen=reslen
               
               
                l=l-1
                r=r+1

        return palin
        