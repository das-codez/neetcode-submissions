class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(b) < len(a):
            a, b = b, a
        total = (len(a) + len(b))
        half = total // 2
        l, r = 0, len(a) - 1
        while True:
            m = (l + r) // 2
            j = half - m - 2

            a_left = a[m] if m >= 0 else float('-infinity')
            a_right = a[m + 1] if (m + 1) < len(a) else float('infinity')
            b_left = b[j] if j >= 0 else float('-infinity')
            b_right = b[j + 1] if (j + 1) < len(b) else float('infinity')

            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                r = m - 1
            else:
                l = m + 1