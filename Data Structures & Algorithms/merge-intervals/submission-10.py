class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = []

        prev = intervals[0]

        for i in range(1, len(intervals)):
            if prev[1] < intervals[i][0]:
                res.append(prev)
                prev = intervals[i]
            else:
                prev = [min(intervals[i][0], prev[0]), max(intervals[i][1], prev[1])]
        
        res.append(prev)
        return res