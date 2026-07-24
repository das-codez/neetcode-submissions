class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for word in strs:
            char = [0] * 26
            for c in word:
                char[ord(c) - ord("a")]+=1
            ans[tuple(char)].append(word)
        return ans.values()