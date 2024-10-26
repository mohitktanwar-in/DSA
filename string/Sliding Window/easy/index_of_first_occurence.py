class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        #if both of them are same, return 0
        if needle == haystack:
            return 0
        #we will use moving window pattern
        n, h = len(needle), len(haystack)

        #as i increases, our window will move fwd.
        for i in range(n, h+1):
            #i-n will increment as i increases but n remains constant, thus, our window remains same size
            if needle == haystack[i-n:i]:
                return i-n
        else:
            return -1