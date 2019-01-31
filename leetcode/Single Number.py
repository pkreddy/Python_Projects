class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in range(len(nums)):
            if d.get(nums[i]) is None:
                d[nums[i]] = 1
            else:
                d[nums[i]] +=1
        a = [str(k) for (k,v) in d.items() if v==1]
        return (int(''.join(a)))
