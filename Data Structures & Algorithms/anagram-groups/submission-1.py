class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            freq[sorted_word].append(word)

        res = []

        for value in freq.values():
            res.append(value)
        return res
        
