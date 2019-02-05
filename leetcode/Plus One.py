class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #print(sum(digits[len(digits)-1:len(digits)] , [1]))
        return ([int(i) for i in (str(int(''.join(map(str,digits))) + 1))])
        #digits = digits + list(map(int, list(str(digits.pop() + 1))))
        #digits.append()
        #return digits