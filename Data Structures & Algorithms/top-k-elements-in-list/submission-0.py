class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, v in freq.items():
            heapq.heappush(minHeap, (v, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        for count, key in minHeap:
            res.append(key)
        
        return res