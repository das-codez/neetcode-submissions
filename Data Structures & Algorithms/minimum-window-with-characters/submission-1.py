class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or (s.isupper() and t.islower()) or (s.islower() and t.isupper()):
            return ""
        lower = True
        new_t = t.lower()
        if t != new_t:
            s,t = s.lower(), t.lower()
            lower = False
        
        # Initialize counters
        required = [0] * 26
        window = [0] * 26
        for c in t:
            required[ord(c) - ord('a')] += 1
        
        q = deque()
        l = 0
        formed = 0
        required_chars = sum(1 for count in required if count > 0)
        min_len = float('inf')
        ans = ""

        for r in range(len(s)):
            c = s[r]
            idx = ord(c) - ord('a')
            if required[idx] > 0:
                window[idx] += 1
                if window[idx] == required[idx]:
                    formed += 1
                q.append(r)

            # Try to shrink the window
            while formed == required_chars:
                # Update the answer
                start = q[0]
                end = r
                if (end - start + 1) < min_len:
                    min_len = end - start + 1
                    ans = s[start:end + 1]

                # Pop from the left
                pop_char = s[q.popleft()]
                pop_idx = ord(pop_char) - ord('a')
                if required[pop_idx] > 0:
                    if window[pop_idx] == required[pop_idx]:
                        formed -= 1
                    window[pop_idx] -= 1

        return ans if lower else ans.upper()
            
            