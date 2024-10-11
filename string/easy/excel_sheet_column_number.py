class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        rev_col = columnTitle[::-1]
        res = 0
        for i, y in enumerate(rev_col):
            res+=pow(26,i)*(ord(y)-ord('A')+1)
        return res