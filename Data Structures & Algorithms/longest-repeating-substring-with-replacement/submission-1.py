class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxF = float('-inf')
        res = 0

        l = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxF = max(maxF, freq[s[r]])

            while (r - l + 1) - maxF > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res