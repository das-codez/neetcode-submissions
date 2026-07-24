class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans+= 1 if n & 1 else 0
            n >>= 1
        return ans