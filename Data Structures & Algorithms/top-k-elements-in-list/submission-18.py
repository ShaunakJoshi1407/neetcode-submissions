class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        min_heap = []
        for key, val in freq.items():
            heapq.heappush(min_heap, (val, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        res = []
        for val, key in min_heap:
            res.append(key)
        
        return res