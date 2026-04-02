class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        dicti_p={}
        dicti={}
        arr=[]
        l=0
        k=len(p)


        for r, char in enumerate(p):
            dicti_p[char]=dicti_p.get(char, 0) + 1

        for r, char in enumerate(s):
            dicti[char]=dicti.get(char, 0)+1

            if r >=k: #if the window length is more than the length of the p
                leftchar=s[r-k]

                dicti[leftchar]-=1

                if dicti[leftchar]==0:
                    del dicti[leftchar]
                    l=l+1

            if dicti==dicti_p:
                arr.append(r-k+1)  

        return arr


        
