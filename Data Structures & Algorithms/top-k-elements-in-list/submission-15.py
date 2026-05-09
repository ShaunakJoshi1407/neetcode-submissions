class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = defaultdict(list)

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, val in freq.items():
            count[val].append(key)
        
        res = []
        for i in range(len(nums), 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res