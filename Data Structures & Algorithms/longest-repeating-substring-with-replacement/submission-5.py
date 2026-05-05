class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxF = 0

        max_len = 0

        l = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            maxF = max(maxF, freq[s[r]])

            while ((r - l + 1) - maxF) > k:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len