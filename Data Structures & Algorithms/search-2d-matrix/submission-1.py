class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat_list = [item for sublist in matrix for item in sublist ]
        l, r = 0, len(mat_list) - 1
        while l <= r:
            m = (l + r)//2
            if mat_list[m] == target:
                return True
            elif mat_list[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False