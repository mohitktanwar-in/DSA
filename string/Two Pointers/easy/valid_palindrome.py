class Solution:
    def isPalindrome(self, s: str) -> bool:
        #if string is empty or has one character, then it is a palindrome
        if len(s) <= 1:
            return True
        
        new_string = list(filter(lambda x: x.isalnum(), s))
        i, j = 0, len(new_string)-1
        #pointers should not cross each other
        while i <= j:
            #if characters don't match then it is not a palindrome
            if new_string[i].lower() != new_string[j].lower():
                return False
            i+=1
            j-=1
        return True