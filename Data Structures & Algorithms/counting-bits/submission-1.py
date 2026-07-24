class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            num = i
            while num:
                ans[i] += 1 if num & 1 else 0
                num >>= 1
        return ans
                
