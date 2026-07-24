class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = {}

        for char in s:
            freq[char] = 1 + freq.get(char, 0)
        
        for char in t:
            freq[char] = freq.get(char, 0) - 1
        
        for val in freq.values():
            if val != 0:
                return False
        
        return True