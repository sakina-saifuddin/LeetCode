class Solution:
    def reverseVowels(self, s: str) -> str:

        i=0
        j=0
        vowels=[]
        newstr=[]

        for char in s[::-1]:
            if char in "aeiouAEIOU":
                vowels.append(char)

        while i < len(s):

            if s[i] in "aeiouAEIOU":
                newstr.append(vowels[j])
                j=j+1
            else:
                newstr.append(s[i])

            i=i+1

        strr="".join(newstr)

 

        return strr




        