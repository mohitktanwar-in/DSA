class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # # isomorphic strings should have same length
        # if len(s) != len(t):
        #     return False
        # else:
        #     # making a dictionary to store corresponding characters in strings
        #     mp = {}
        #     for i, y in zip(s,t):
        #         # if value is already assigned to a key in dict
        #         if y in mp.values():
        #             # if existing key value pair is same then skip
        #             if i in mp.keys():
        #                 pass
        #             # else different key value pair is trying to form
        #             else:
        #                 return False
        #         # value is not in dict yet, so add the key value pair
        #         else:
        #             mp[i] = y
        #     x = ""
        #     # create new string using dict
        #     for i in s:
        #         x+=mp[i]
        #     # check if created string matches the other string
        #     if x == t:
        #         return True
        #     else:
        #         return False
        """ 
        number of unique characters in either strings should match with each
        other as well as number of unique pairs of characters between the two 
        strings. The last part ensures that order is maintained, as if order 
        is not maintained then extra pair(s) will be generated.
        example: s = fototf, t = barabr. Here set(zip(s,t)) will result in,
        (f,b),(o,a),(t,r),(t,b),(f,r).
        Else if it would have been, s = fototf, t = bararb, set(zip(s,t)) will 
        result in,
        (f,b),(o,a),(t,r). Thus, number of unique pairs match with number of 
        unique characters in the both the strings.
        """
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))