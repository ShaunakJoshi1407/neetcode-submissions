class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # intervals ending before newInterval starts
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # intervals that start after newInterval ends
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # overlapping intervals
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1]),]
        
        res.append(newInterval)
        return res
