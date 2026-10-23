class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(capacity):
            total = 0
            D = 1

            for num in nums:
                total += num
                if total > capacity:
                    D += 1
                    if D > k:
                        return False
                    
                    total = num
            return True
        

        l, r = max(nums), sum(nums)
        while l <= r:
            mid = l + (r - l) // 2
            if feasible(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l