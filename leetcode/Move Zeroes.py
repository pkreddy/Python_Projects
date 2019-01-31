class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 1
        i = 0
        while i <= len(nums) - 1:
            if nums[i] == 0:
                nums.pop(i)
                count+=1
                i -= 1
            i+=1

        for _ in range(count-1):
            nums.append(0)
