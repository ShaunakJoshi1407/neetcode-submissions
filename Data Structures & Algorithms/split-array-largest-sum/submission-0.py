class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(threshold):
            count = 1
            total = 0

            for num in nums:
                total += num
                if total > threshold:
                    count += 1
                    total = num
                    if count > k:
                        return False
            
            return True
        
        l, r = max(nums), sum(nums)

        while l < r:
            mid = l + (r - l) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l