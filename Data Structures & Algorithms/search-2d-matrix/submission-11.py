class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l, r = 0, ROWS * COLS

        while l < r:
            mid = l + (r - l) // 2
            row = mid // COLS
            col = mid % COLS

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid
            else:
                l = mid + 1
        
        return False