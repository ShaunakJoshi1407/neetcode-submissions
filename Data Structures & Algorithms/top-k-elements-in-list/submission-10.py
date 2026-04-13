class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        min_heap = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, value in freq.items():
            heapq.heappush(min_heap, (value, key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        

        res = []
        for value, key in min_heap:
            res.append(key)
        
        return res