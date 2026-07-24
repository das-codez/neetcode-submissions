class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dp(first_index, second_index):
            if first_index == len(text1) or second_index == len(text2):
                return 0
            if (first_index, second_index) in memo:
                return memo[(first_index, second_index)]
                
            if text1[first_index] == text2[second_index]:
                memo[(first_index, second_index)] = 1 + dp(first_index + 1,second_index + 1)
            else:
                memo[(first_index, second_index)] = max(dp(first_index + 1, second_index), dp(first_index, second_index + 1))
            return memo[(first_index, second_index)]

        memo = {}
        return dp(0, 0)       