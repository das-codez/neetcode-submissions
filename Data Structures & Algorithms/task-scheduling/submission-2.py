class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans = 0
        counts = Counter(tasks)
        heap = [-cnt for cnt in counts.values()]
        heapq.heapify(heap)

        q = deque()
        while heap or q:
            ans+=1
            if heap:
                count = heapq.heappop(heap) + 1
                if count:
                    q.append([count, ans + n])
            if q and q[0][1] == ans:
                heapq.heappush(heap, q.popleft()[0])
        return ans