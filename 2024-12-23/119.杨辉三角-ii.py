#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# 解题思路:
# 1. 使用滚动数组的思想,只保留一行结果,每次基于上一行计算当前行
# 2. 从后向前计算,避免覆盖需要使用的数据
# 3. 利用杨辉三角的对称性,只需计算一半即可
#
# 使用的数据结构和算法:
# - 数据结构:数组(列表)
# - 算法:动态规划,滚动数组优化
#
# 时间复杂度:O(rowIndex^2) - 需要计算rowIndex行,每行最多rowIndex个数
# 空间复杂度:O(rowIndex) - 只需要保存一行数据

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 初始化结果数组,长度为rowIndex+1
        row = [0] * (rowIndex + 1)
        # 第一个元素始终为1
        row[0] = 1
        
        # 逐行计算,从第1行开始
        for i in range(1, rowIndex + 1):
            # 从后向前计算当前行的每个元素
            for j in range(i, 0, -1):
                # 当前位置的值等于上一行的相同位置和前一个位置的值的和
                row[j] = row[j] + row[j-1]
        
        return row
    

    def generate(self, rowIndex: int) -> List[int]:
        # 初始化结果列表
        res = []
        
        # 遍历每一行
        for i in range(rowIndex + 1):
            # 初始化当前行,首尾都是1
            row = [1] * (i + 1)
            
            # 计算中间的数字
            for j in range(1, i):
                # 当前位置的数字等于上一行相邻两个数的和
                row[j] = res[i-1][j-1] + res[i-1][j]
                
            # 将当前行添加到结果中
            res.append(row)
            
        return row

# @lc code=end
