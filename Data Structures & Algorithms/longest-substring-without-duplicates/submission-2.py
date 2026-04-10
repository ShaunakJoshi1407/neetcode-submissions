class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        l, r = 0, 0

        maxLen = float('-inf')

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen if maxLen != float('-inf') else 0