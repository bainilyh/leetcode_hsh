#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
# 解题思路:
# 将矩阵顺时针旋转90度可以通过两步完成:
# 1. 先沿主对角线翻转(即交换matrix[i][j]和matrix[j][i])
# 2. 再左右翻转每一行(即交换matrix[i][j]和matrix[i][n-1-j])
#
# 数据结构: 二维数组(矩阵)
# 算法: 矩阵变换
#
# 时间复杂度: O(n^2) - 需要遍历整个n*n矩阵
# 空间复杂度: O(1) - 原地修改矩阵,只使用常数额外空间

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)  # 获取矩阵大小
        
        # 沿主对角线翻转
        for i in range(n):
            for j in range(i, n):
                # 交换matrix[i][j]和matrix[j][i]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 左右翻转每一行
        for i in range(n):
            for j in range(n // 2):
                # 交换matrix[i][j]和matrix[i][n-1-j]
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
        
# @lc code=end
