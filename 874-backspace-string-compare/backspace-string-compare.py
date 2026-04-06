class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackstr_s=[]
        stackstr_t=[]
        for i, char in enumerate(s):
            if char == "#":
                if stackstr_s:
                    stackstr_s.pop()
            else:
                stackstr_s.append(char)
            
        sstr="".join(stackstr_s)
        
        for i, char in enumerate(t):
            if char == "#":
                if stackstr_t:
                    stackstr_t.pop()
            else:
                stackstr_t.append(char)
        strt="".join(stackstr_t)
        
        if sstr==strt:
            return True
        else:
            return False
