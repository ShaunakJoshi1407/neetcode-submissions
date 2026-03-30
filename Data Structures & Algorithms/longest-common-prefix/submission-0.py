class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivotWord = strs[0]

        for i in range(1, len(strs)):
            if not pivotWord:
                break
            j = 0
            while j < min(len(pivotWord), len(strs[i])):
                if pivotWord[j] != strs[i][j]:
                    break
                j += 1
            pivotWord = pivotWord[:j]
        return pivotWord