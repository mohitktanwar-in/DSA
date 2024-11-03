class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # """
        # if string is empty, return 0
        # """
        # if len(s) == 0:
        #     return 0
        # if len(set(s)) == 1:
        #     return 1
        # """
        # if all characters are same, first character will be longest substring
        # """
        # lng_substr = s[0]
        # """
        # start with max length equal to 1 bcz we start with first character assuming 
        # as longest substring
        # """
        # max_length = 1
        # """
        # using two pointer method, first at first character, second at next character
        # """
        # i = 0
        # j = 1
        # """
        # second pointer shouldn't go out of string
        # """
        # while j < len(s):
        #     """
        #     if char is repeated, increment first pointer by 1 and 
        # move second pointer to next character, just like how we started 
        # at first character in the beginning
        #     """
        #     if s[j] in lng_substr:
        #         i+=1
        #         lng_substr = s[i]
        #         j=i+1
        #         """
        #         add the character to longest substr and check if length of that 
        # exceeds previous max length encountered. If greater, assign its length to max length
        #         """
        #     else:
        #         lng_substr+=s[j]
        #         if len(lng_substr) > max_length:
        #             max_length = len(lng_substr)
        #         j+=1
        # return max_length
        """
        Better Approach:
        Initialize everything as 0. We will build everything as we iterate through 
        the string. We will need to take note of max_length, length of substring, 
        position of two pointers, first one keeps note of starting point of substring,
         second keeps moving through the string one by one and a dictionary to keep 
         track of location of characters we encounter so that we can compare and 
         adjust starting point of substring if we encounter a repeated character.
        """
        max_length = 0
        # lng_substr = ""
        substr_len = 0
        chr_dict = {}
        i = 0
        for j, y in enumerate(s):
            """
            if we encounter a repeated character and that is in the current sub string, 
            we change the start pointer to point at the next character to location stored 
            in dict of the repeated character. That becomes our new start pointer. Also we 
            update location of the character in dict with location of repeated character. 
            Length of substring now becomes length of substr from new start pointer to 
            current pointer which is at repeated character.
            """
            if y in chr_dict and chr_dict[y] >= i:
                i=chr_dict[y]+1
                chr_dict[y] = j
                # lng_substr=s[i:j+1]
                substr_len = len(s[i:j+1])
            else:
                """
            New character needs to be added to dictionary with its location in string. 
            length of substring increments by 1 and we check if substring length became 
            larger than max length encountered till now.
                """
                chr_dict[y]=j
                # lng_substr+=y
                substr_len+=1
                if substr_len > max_length:
                    max_length=substr_len
        return max_length