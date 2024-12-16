#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# 解题思路:
# 1. 创建一个n x n的矩阵，按照顺时针螺旋顺序填入1到n^2的数字
# 2. 使用四个变量left, right, top, bottom来控制边界
# 3. 按照右->下->左->上的顺序填充数字
# 4. 每填充完一条边，相应的边界就要收缩
# 
# 使用的数据结构:
# - 二维列表(矩阵)
#
# 使用的算法:
# - 模拟法
#
# 时间复杂度: O(n^2) - 需要填充n^2个格子
# 空间复杂度: O(1) - 不考虑返回值的空间，只需要常数个变量

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 初始化n x n的矩阵，填充0
        matrix = [[0] * n for _ in range(n)]
        
        # 定义四个边界
        left, right = 0, n-1
        top, bottom = 0, n-1
        
        # 当前要填入的数字
        num = 1
        
        while num <= n*n:
            # 从左到右填充上边
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            
            # 从上到下填充右边
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            # 从右到左填充下边
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            
            # 从下到上填充左边
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        
        return matrix

# @lc code=end
