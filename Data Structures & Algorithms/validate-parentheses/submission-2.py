class Solution:
    def isValid(self, s: str) -> bool:
        myMap = {"}": "{", "]":"[", ")":"("}
        stack = []

        for c in s:
            if c in myMap:
                if stack and stack[-1] == myMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False