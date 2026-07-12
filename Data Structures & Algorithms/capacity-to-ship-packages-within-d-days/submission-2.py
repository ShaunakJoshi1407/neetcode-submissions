class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            D = 1
            total = 0

            for w in weights:
                total += w
                if total > capacity:
                    total = w
                    D += 1
                    if D > days:
                        return False
            
            return True

        l, r = max(weights), sum(weights)

        while l < r:
            mid = l + (r - l) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        
        return l