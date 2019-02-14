class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return -1
        
        s = s.encode('utf-8')
        present = {}
        for i in range(len(s)):
            if s[i] in present:
                if present[s[i]] is not -1:
                    present[s[i]] = -1
            else:
                present[s[i]] = i
                
        for k,v in present.items():
            if v == -1:
                del present[k]
        
        present = sorted(present.items(), key=operator.itemgetter(1))
        if not present:
            return -1
        return(int(present[0][1]))
        #return(int((sorted(present.items(), key=lambda x: x[1])[0])[1]))