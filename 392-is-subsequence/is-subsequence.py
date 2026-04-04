# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:

#         new_s=[]
#         new_t=[]
#         newarr=[]
#         j=0
#         newstr=""

#         for i, char in enumerate(s):
#             new_s.append(char)

#         for i, char in enumerate(t):
#             new_t.append(char)

#         while j < len(new_t):

#             if new_t[j] in new_s:
#                 newarr.append(new_t[j])

#             newstr="".join(newarr)
#             print(newstr)
#             if len(newarr)==len(new_s) and newstr==s:
#                 return True

#             if len(newarr)==len(new_s) and newstr!=s:
#                 print("deleting")
#                 del newarr[:]
        

            

#             j=j+1

#         if newstr==s:
#             return True
#         else:
#             return False


class Solution:
     def isSubsequence(self, s: str, t: str) -> bool:

        j=0
        i=0

        while i<len(s) and j< len(t):
            if s[i]==t[j]:
                i=i+1
            j=j+1
        
        if i==len(s):
            return True
        else:
            return False