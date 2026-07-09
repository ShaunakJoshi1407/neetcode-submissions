"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        freq = defaultdict(int)

        for i in intervals:
            freq[i.start] += 1
            freq[i.end] -= 1
        
        prev = 0
        res = 0
        for i in sorted(freq.keys()):
            prev += freq[i]
            res = max(prev, res)
        
        return res