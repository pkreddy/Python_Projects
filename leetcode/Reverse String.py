class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        l = len(s)
        l2 = l-1
        for i in range(l/2):
            l2 = l-i-1
            s[i],s[l2] = s[l2],s[i]