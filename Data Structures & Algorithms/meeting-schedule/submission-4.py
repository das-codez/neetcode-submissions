"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        start_stop = [0] * 10000001
        for interval in intervals:
            start_stop[interval.start]+=1
            start_stop[interval.end]-=1
        curr = 0
        for val in start_stop:
            curr+=val
            if curr > 1:
                return False
        return True