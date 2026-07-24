class Solution:
    def isValid(self, s: str) -> bool:
        parDict = {"}":"{", ")":"(", "]": "["}
        stack = []
        for c in s:
            if c not in parDict:
                stack.append(c)
            elif not stack:
                return False
            else:
                curr = stack.pop()
                if parDict[c] != curr:
                    return False

        return True if not stack else  False
        