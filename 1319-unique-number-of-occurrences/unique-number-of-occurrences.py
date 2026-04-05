class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        dicti={}
        for i in range(len(arr)):
            dicti[arr[i]]=dicti.get(arr[i], 0)+1

        valueset=set(dicti.values())
        print(valueset)

        if len(valueset)==len(dicti):
            return True
        else:
            return False
        