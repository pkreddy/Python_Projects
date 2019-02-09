class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= -2147483648:
            return 0
        elif x > 2147483647:
            return 0
        else:
            negative = 1
            if x < 0:
                negative = -1
                x = x * -1

            x = list(str(x))
            l = len(x)
            l2 = l-1
            for i in range(l/2):
                l2 = l-i-1
                x[i],x[l2] = x[l2],x[i]
        y = int(''.join(x)) * negative
        if y <= -2147483648:
            return 0
        elif y > 2147483647:
            return 0
        else:
            return y
        
            #return int(''.join(x)) * negative
    