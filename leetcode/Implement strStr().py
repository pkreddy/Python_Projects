class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h = len(haystack)
        n = len(needle)
        if haystack == needle:
            return 0
        else:
            for i in range(h - n + 1):
                if haystack[i:i+n] == needle:
                    return i
        
        return -1
                