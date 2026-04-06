class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-stone for stone in stones]
        heapq.heapify(minHeap)

        
        while len(minHeap) > 1:
            firstVal = -heapq.heappop(minHeap)
            secondVal = -heapq.heappop(minHeap)

            if firstVal != secondVal:
                heapq.heappush(minHeap, -(firstVal - secondVal))
            else:
                continue
        
        return -minHeap[0] if len(minHeap) > 0 else 0
