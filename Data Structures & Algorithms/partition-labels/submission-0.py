class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        counts = Counter(list(s))
        seen = set()
        curr = 0
        ans = []
        for c in s:
            counts[c]-=1
            curr+=1
            if counts[c] > 0 and c not in seen:
                seen.add(c)
            elif counts[c] == 0:
                if c in seen:
                    seen.remove(c)
                if len(seen) == 0:
                    ans.append(curr)
                    curr = 0
        return ans
