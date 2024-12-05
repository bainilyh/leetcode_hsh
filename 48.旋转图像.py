#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        顺时针旋转90度，先对角线兑换，然后沿中间线对换
        """
        def swap(matrix, i, j, k, l):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[k][l]
            matrix[k][l] = tmp
        
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(i + 1, m): #这里为什么是i + 1可以思考下
                swap(matrix, i, j, j, i)
                
        for i in range(n):
            for j in range(m // 2):
                swap(matrix, i, j, i, m - j - 1)
            
        
# @lc code=end

