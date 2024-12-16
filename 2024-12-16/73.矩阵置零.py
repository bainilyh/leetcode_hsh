#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
# 解题思路:
# 1. 使用第一行和第一列作为标记数组
# 2. 先记录第一行和第一列是否原本包含0
# 3. 遍历矩阵,如果某个元素为0:
#    - 将对应的第一行和第一列的元素置为0作为标记
# 4. 根据第一行和第一列的标记,将对应行和列置0
# 5. 最后根据原始状态处理第一行和第一列
#
# 数据结构:
# - 二维数组: 矩阵
# - 布尔值: 记录第一行和第一列的原始状态
#
# 时间复杂度: O(mn), m和n分别为矩阵的行数和列数
# 空间复杂度: O(1), 只使用常数额外空间

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 获取矩阵的行数和列数
        m, n = len(matrix), len(matrix[0])
        
        # 记录第一行和第一列是否原本包含0
        first_row_has_zero = False
        first_col_has_zero = False
        
        # 检查第一行是否有0
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break
                
        # 检查第一列是否有0
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
                
        # 使用第一行和第一列作为标记
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # 根据标记将对应行和列置0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # 处理第一行
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
                
        # 处理第一列
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
        
# @lc code=end
