#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#
# 解题思路:
# 1. 由于矩阵的特性(每行从左到右升序,每行第一个数大于上一行最后一个数)
# 2. 可以将二维矩阵看作一个一维有序数组,使用二分查找
# 3. 关键是二维坐标和一维索引的转换:
#    - 一维索引 i 转二维坐标: row = i // n, col = i % n
#    其中n为矩阵的列数
# 
# 使用算法: 二分查找
# 使用数据结构: 数组

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 特判: 矩阵为空或矩阵第一行为空
        if not matrix or not matrix[0]:
            return False
            
        # 获取矩阵的行数和列数
        m, n = len(matrix), len(matrix[0])
        
        # 在[0, m*n-1]范围内进行二分查找
        left, right = 0, m * n - 1
        
        while left <= right:
            # 计算中间位置
            mid = (left + right) // 2
            # 将一维索引转换为二维坐标
            row, col = mid // n, mid % n
            # 获取中间位置的值
            num = matrix[row][col]
            
            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False

# @lc code=end
# 时间复杂度: O(log(m*n)), 其中m和n分别是矩阵的行数和列数
# 空间复杂度: O(1), 只使用了常数额外空间
