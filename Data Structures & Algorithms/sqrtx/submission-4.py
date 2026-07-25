class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 2:
            return x
        
        l, r = 0, x // 2
        res = 0

        while l <= r:
            mid = l + (r - l) // 2
            prod = mid * mid

            if prod == x:
                return mid
            elif prod < x:
                l = mid + 1
                res = mid
            else:
                r = mid - 1
        
        return res
