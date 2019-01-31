class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        j = 0
        for i in range(len(nums1)):
            while j < len(nums2):
                if nums1[i] == nums2[j]:
                    result.append(nums2.pop(j))
                    break
                j+=1
            j = 0
        return result
