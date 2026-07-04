class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = []

        for num, start, end in trips:
            points.append([start, num])
            points.append([end, -num])
        
        points.sort()

        curr = 0
        for point, passengers in points:
            curr += passengers
            if curr > capacity:
                return False
        
        return True