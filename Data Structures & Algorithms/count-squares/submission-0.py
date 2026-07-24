class CountSquares:

    def __init__(self):
        self.counts = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.counts[tuple(point)] += 1
        self.pts.append(point)
    def count(self, point: List[int]) -> int:
        ans = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px-x)) or x == px or y == py:
                continue
            ans += self.counts[(x, py)] * self.counts[(px, y)]
        return ans
            
