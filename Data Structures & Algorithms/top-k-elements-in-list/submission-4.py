class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        minHeap = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1


        for key, val in freq.items():
            heapq.heappush(minHeap, (val, key))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        for value, key in minHeap:
            res.append(key)
        
        return res