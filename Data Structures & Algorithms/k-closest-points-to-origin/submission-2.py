class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        res = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            heapq.heappush(min_heap, ([dist, x, y]))
        
        for _ in range(k):
            dist, x, y = heapq.heappop(min_heap)
            res.append((x, y))

        
        return res