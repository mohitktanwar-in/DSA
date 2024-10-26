class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        
        while columnNumber > 0:
            columnNumber-=1
            print(columnNumber)
            res+= chr(65+(columnNumber%26))
            columnNumber = columnNumber//26
        return(res[::-1])