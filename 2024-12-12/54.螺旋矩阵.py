#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# 解题思路:
# 1. 使用四个指针表示当前要遍历的上下左右边界
# 2. 按照右->下->左->上的顺序遍历矩阵
# 3. 每遍历完一个方向后,相应的边界向内收缩一格
# 4. 直到所有元素都被遍历完
#
# 数据结构: 数组
# 算法: 模拟、边界处理
#
# 时间复杂度: O(m*n), m和n分别是矩阵的行数和列数,需要遍历所有元素
# 空间复杂度: O(1), 只使用了常数个变量

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 处理空矩阵的情况
        if not matrix or not matrix[0]:
            return []
        
        # 初始化结果列表
        result = []
        
        # 定义四个边界
        left, right = 0, len(matrix[0]) - 1  # 左右边界
        top, bottom = 0, len(matrix) - 1      # 上下边界
        
        while True:
            # 从左到右遍历
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # 上边界下移
            if top > bottom:
                break
                
            # 从上到下遍历    
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # 右边界左移
            if left > right:
                break
                
            # 从右到左遍历
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1  # 下边界上移
            if top > bottom:
                break
                
            # 从下到上遍历
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1  # 左边界右移
            if left > right:
                break
                
        return result
        
# @lc code=end
