class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        #assume first string in list as common prefix
        cmn = strs[0]
        #loop through all other strings in the list
        for i in strs[1:]:
            #if common prefix is not present in the string, reduce length of prefix by 1 and then check again. Do it till the prefix is found or reduced to empty string
            while i.find(cmn) != 0:
                cmn = cmn[:-1]
            if len(cmn) == 0:
                return cmn
        return cmn