class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        half = (m+n+1)//2
        left,right=0,m
        while left <= right:
            i=(left+right)//2
            j=half-i
            nums1_left  = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i]     if i < m else float('inf')
            nums2_left  = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j]     if j < n else float('inf')
            if nums1_left>nums2_right:
                right=i-1
            elif nums2_left >nums1_right:
                left=i+1
            else:
                left_max = max(nums1_left, nums2_left)
                right_min = min(nums1_right, nums2_right)

                if (m + n) % 2 == 1:
                    return float(left_max)
                return (left_max + right_min) / 2.0
        return 0.0
