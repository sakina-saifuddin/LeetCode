class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dicti_s1={}
        dicti_s2={}
        k=len(s1)
        result=False

        for i, char in enumerate(s1):
            dicti_s1[char]=dicti_s1.get(char, 0) +1


        for r, char in enumerate(s2):
            dicti_s2[char]=dicti_s2.get(char,0)+1

            if r>=k:
                leftchar=s2[r-k]

                dicti_s2[leftchar]-=1 

                if dicti_s2[leftchar]==0:
                    del dicti_s2[leftchar]

            if dicti_s1==dicti_s2:
                result=True

        return result
            


        