class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        l = top = 0
        r, bottom = len(matrix[0]) - 1, len(matrix) - 1

        while l <= r and top <= bottom:
            for col in range(l, r + 1):
                ans.append(matrix[top][col])
            top+=1

            for row in range(top, bottom + 1):
                ans.append(matrix[row][r])
            r-=1

            if not (l <= r and top <= bottom):
                break
            
            for col in range(r, l - 1, -1):
                ans.append(matrix[bottom][col])
            bottom-=1

            for row in range(bottom, top - 1, -1):
                ans.append(matrix[row][l])
            l+=1
        return ans