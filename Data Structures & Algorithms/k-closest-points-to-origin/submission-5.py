class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        res = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            min_heap.append([dist,x,y])
        
        heapq.heapify(min_heap)

        for i in range(k):
            _, x, y = heapq.heappop(min_heap)
            res.append([x, y])
        
        return res