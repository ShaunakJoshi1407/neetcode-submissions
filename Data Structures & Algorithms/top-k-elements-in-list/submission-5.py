class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        minHeap = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, value in freq.items():
            heapq.heappush(minHeap, (value, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        for value, key in minHeap:
            res.append(key)
        
        return res