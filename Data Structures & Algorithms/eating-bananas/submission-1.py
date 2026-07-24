class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(rate):
            ans = 0
            for pile in piles:
                ans+=math.ceil(pile/rate)
            return ans <= h
        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            if check(m):
                r = m - 1
            else: 
                l = m + 1
        return l