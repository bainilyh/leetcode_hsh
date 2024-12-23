#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# 解题思路:
# 1. 杨辉三角的每一行首尾都是1
# 2. 中间的每个数是上一行相邻两个数的和
# 3. 使用动态规划,每一行基于上一行计算
#
# 使用的数据结构和算法:
# - 二维列表存储结果
# - 动态规划

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 初始化结果列表
        res = []
        
        # 遍历每一行
        for i in range(numRows):
            # 初始化当前行,首尾都是1
            row = [1] * (i + 1)
            
            # 计算中间的数字
            for j in range(1, i):
                # 当前位置的数字等于上一行相邻两个数的和
                row[j] = res[i-1][j-1] + res[i-1][j]
                
            # 将当前行添加到结果中
            res.append(row)
            
        return res

# @lc code=end

# 时间复杂度: O(n^2), n为行数,需要遍历每一行的每个元素
# 空间复杂度: O(n^2), 需要存储n行数据,每行最多n个元素
