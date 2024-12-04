#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def get(index, matrix):
            l = index // len(matrix[0])
            r = index % len(matrix[0])
            return matrix[l][r]
        
        n, m = len(matrix), len(matrix[0])
        left, right = 0, n * m - 1
        while left <= right:
            mid = left + (right - left) // 2
            target_ = get(mid, matrix)
            if target_ == target:
                return True
            elif target_ > target:
                right = mid - 1
            elif target_ < target:
                left = mid + 1
        return False
# @lc code=end

