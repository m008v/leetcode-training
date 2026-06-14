class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        i, j = 0, 1
        for ia in range(i, len(nums)):
            for ja in range(j, len(nums)):
                ii = nums[ia]
                ji = nums[ja]
                if (ii > ji):
                    nums[ia] = ji
                    nums[ja] = ii
            j += 1
        total = len(nums)
        if total % 2 == 1:
            return float(nums[total // 2])
        middle_1 = nums[total // 2]
        middle_2 = nums[total // 2 - 1]
        t = (float(middle_1) + float(middle_2)) / 2.0 
        return t

X = Solution()
print(X.findMedianSortedArrays([1, 3], [2, 7]))