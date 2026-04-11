class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]

        hashmap={"}":"{", "]":"[", ")":"("}

        for char in s:

            if char in hashmap:

                if not stack or stack[-1]!=hashmap[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack)==0

            

                






















        # stack=[]

        # hashmap={")":"(", "}":"{", "]":"["}

        # for brac in s:
        #     if brac in hashmap:

        #         if not stack or stack[-1]!=hashmap[brac]:
        #             return False
        #         stack.pop()

        #     else:
        #         stack.append(brac)


        # return len(stack)==0





















        # stack=[]
        # hashmap={")":"(", "]":"[", "}":"{"}
        

        # for char in s:
        #     if char in hashmap: #then pop
        #         if not stack or stack[-1]!=hashmap[char]:
        #             return False
        #         stack.pop()

        #     else: #then append
        #         stack.append(char)

        # return len(stack)==0















              
        