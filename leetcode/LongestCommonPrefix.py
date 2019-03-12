class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        """
        common = ""
        for j in range(len(strs[0])):
            add_common = strs[0][j]
            for i in range(len(strs)-2):
                if strs[i][j] <> strs[i+1][j]:
                    add_common = ""
                common = common + add_common
        return common
        """
        if strs == []:
            return ""
        if len(strs)==1:
            return ''.join(strs)
        l = len(min(strs,key=len))
        if l == 0:
            return ""
        common = ""
        for j in range(l):
            add_common = strs[0][j]
            for i in range(len(strs)-1):
                if strs[i][j] <> strs[i+1][j]:
                    return common
            common = common + add_common
        return common