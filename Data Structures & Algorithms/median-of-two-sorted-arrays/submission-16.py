import bisect

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        half = (m+n) // 2

        l = 0
        r = m - 1
        
        while True:
            i = l + (r-l) // 2
            j = half - i - 2
            print(i, j)

            left1 = nums1[i] if i >= 0 else float('-inf')
            right1 = nums1[i+1] if i < m-1 else float('inf')
            left2 = nums2[j] if j >= 0 else float('-inf')
            right2 = nums2[j+1] if j < n-1 else float('inf')

            if left1 <= right2 and left2 <= right1:
                if (m+n) % 2 == 0:
                    return (min(right1, right2) + max(left1, left2)) / 2
                else:
                    return min(right1, right2)
            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1