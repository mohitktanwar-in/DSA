class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]

        n = max(len(a), len(b))

        carry = 0

        res = ""

        for i in range(n):
            if i >= len(a):
                x = '0'
            else:
                x = a[i]
            if i >= len(b):
                y = '0'
            else:
                y = b[i]
            quo = (int(x)+int(y)+carry)//2
            rem = (int(x)+int(y)+carry)%2
            res+=str(rem)
            carry = quo

        if carry:
            res+="1"
        return res[::-1]