class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack=[]
        result=[]
        nextgreater={}

        for num in nums2:

            while stack and num>stack[-1]:
                smaller=stack.pop()
                nextgreater[smaller]=num

            stack.append(num)



            if not stack:
                stack.append(num)

        while stack:
            smaller=stack.pop()
            nextgreater[smaller]=-1

        print(nextgreater)

        

        for n in nums1:
            print("n", n)
            if nextgreater:
                print(nextgreater[n])
                result.append(nextgreater[n])
        return result






        # stack=[]
        # dicti={}
        # result=[]

        # for num in nums2:


        #     while stack and num>stack[-1]:
        #         smaller=stack.pop()
        #         dicti[smaller]=num

        #     stack.append(num)



        # while stack:
        #     dicti[stack.pop()]=-1

        # print(dicti)

        # for n in nums1:
        #     result.append(dicti[n])

        # return result
        