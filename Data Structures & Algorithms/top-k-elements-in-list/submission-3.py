class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        freq = {}
        count = defaultdict(list)

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, value in freq.items():
            count[value].append(key)
        
        res = []
        for i in range(len(nums), 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res