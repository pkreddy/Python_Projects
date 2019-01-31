class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            o_target = target - nums[i]
            for j in range(i+1,len(nums)):
                if o_target == nums[j]:
                    return [i,j]

                
