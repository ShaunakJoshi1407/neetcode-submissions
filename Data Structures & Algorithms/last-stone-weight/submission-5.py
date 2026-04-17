class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = [-stone for stone in stones]
        heapq.heapify(min_heap)

        while len(min_heap) > 1:
            first = -heapq.heappop(min_heap)
            second = -heapq.heappop(min_heap)

            if first != second:
                heapq.heappush(min_heap, -(first - second))
            else:
                continue

        return -min_heap[0] if len(min_heap) > 0 else 0