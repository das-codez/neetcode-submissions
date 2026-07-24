"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        overlaps = [0] * 1_000_001
        for interval in intervals:
            overlaps[interval.start]+=1
            overlaps[interval.end]-=1
        
        cur = ans = 0
        for overlap in overlaps:
            cur+=overlap
            ans = max(cur, ans)
        return ans