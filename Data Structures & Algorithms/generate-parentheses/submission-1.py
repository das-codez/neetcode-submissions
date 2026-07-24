class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(opened, closed):
            if opened == closed == 0:
                res.append("".join(stack))
                return

            if opened > 0:
                stack.append("(")
                backtrack(opened - 1, closed)
                stack.pop()
            if opened < closed:
                stack.append(")")
                backtrack(opened, closed - 1)
                stack.pop()
        backtrack(n, n)
        return res

