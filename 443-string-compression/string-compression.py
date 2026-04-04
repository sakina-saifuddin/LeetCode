class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        j=0
        count=0
        write=0

        while i < len(chars):
            char=chars[i] #char="a"
            j=i
            count=0

            while j < len(chars) and char==chars[j]:
                count=count+1
                j=j+1

            chars[write]=char
            write=write+1
        


            if count > 1:
                for r in str(count):
                    chars[write]=r
                    write=write+1
            i=j

        return write

        