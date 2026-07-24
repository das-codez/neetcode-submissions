class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        ans = l = 0
        for r, c in enumerate(s):
            counts[c]+=1
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]]-=1
                l+=1
            ans = max(ans, r - l + 1)
        return ans
