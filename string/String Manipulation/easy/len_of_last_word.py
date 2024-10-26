class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        #loop in reverse order
        for i in s[::-1]:
            if i != " ":
                print(i)
                count+=1
            #if we have iterated the last word and then space comes, return count
            elif count != 0 and i == " ":
                return count
            #if we have not iterated through the last word and space is encountered, do nothing
            else:
                continue
        else:
            return count
        # #convert string to list and calculate length of last element
        # return len(s.strip().split()[-1])