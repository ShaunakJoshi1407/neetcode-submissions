class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def feasible(capacity):
            curr_sum = 0
            count = 1

            for num in nums:
                curr_sum += num
                if curr_sum > capacity:
                    count += 1
                    if count > k:
                        return False
                    
                    curr_sum = num
            
            return True
        
        l, r = max(nums), sum(nums)

        while l < r:
            mid = l + (r - l) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l