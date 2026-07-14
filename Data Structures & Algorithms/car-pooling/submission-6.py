class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = []

        for num, start, end in trips:
            points.append([start, num])
            points.append([end, -num])
        
        points.sort()
        curr = 0

        for point, num in points:
            curr += num
            if curr > capacity:
                return False

        return True