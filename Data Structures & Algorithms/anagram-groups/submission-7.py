class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for c in word:
                counts[ord(c) - ord('a')]+=1
            ans[tuple(counts)].append(word)
        return list(ans.values())
                

        