class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def valid(row, col):
            return 0 <= row < n and 0 <= col < n
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(grid)
        heap = [[grid[0][0], 0, 0]]
        seen = set()
        while heap:
            time, r, c = heapq.heappop(heap)
            seen.add((r, c))
            if r == n - 1 and c == n - 1:
                return time
            for dr, dc in dirs:
                row, col = r + dr, c + dc
                if (row, col) not in seen and valid(row, col):
                    heapq.heappush(heap, [max(time, grid[row][col]), row, col])
