class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxF = float('-inf')

        l, r = 0, 0
        max_len = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxF = max(maxF, freq[s[r]])

            if ((r - l + 1) - maxF) > k:
                freq[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, (r - l + 1))
        
        return max_len
