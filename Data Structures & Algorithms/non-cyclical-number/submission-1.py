class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_squares(n):
            ans = 0
            while n:
                digit = n % 10
                digit = digit ** 2
                ans+=digit
                n//=10
            return ans
        visit = set()
        while n not in visit:
            visit.add(n)
            n = sum_squares(n)
            if n == 1:
                return True
        return False