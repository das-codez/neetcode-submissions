class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()  # Stores *indices* of useful elements in decreasing order

        for r in range(len(nums)):
            # Remove smaller elements from the back
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # Remove the front element if it's outside the window
            if q[0] <= r - k:
                q.popleft()

            # Append the max once the first full window is formed
            if r >= k - 1:
                ans.append(nums[q[0]])

        return ans