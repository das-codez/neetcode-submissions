class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n == 0:
                return 1
            if x == 0:
                return 0
            ans = helper(x, n // 2)
            ans*=ans
            return ans * x if n % 2 else ans
        ans = helper(x, abs(n))
        return ans if n >= 0 else 1/ans