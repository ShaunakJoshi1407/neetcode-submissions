class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            if prev[1] >= intervals[i][0]:
                prev = [min(prev[0], intervals[i][0]), max(prev[1], intervals[i][1])]
            else:
                res.append(prev)
                prev = intervals[i]
        
        res.append(prev)
        return res