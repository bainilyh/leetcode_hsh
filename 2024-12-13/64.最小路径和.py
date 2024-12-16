#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# 解题思路:
# 1. 这是一个动态规划问题,需要找到从左上角到右下角的最小路径和
# 2. 每个格子只能向右或向下移动,到达某个格子的最小路径和等于到达其上方格子或左方格子的最小路径和加上当前格子的值
# 3. 使用二维数组dp[i][j]表示到达(i,j)位置的最小路径和
# 4. 第一行和第一列的格子只有一种到达方式,需要特殊处理
# 5. 其他格子的最小路径和为: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
#
# 数据结构: 二维数组(矩阵)
# 算法: 动态规划
#
# 时间复杂度: O(m*n) - 需要遍历整个矩阵
# 空间复杂度: O(m*n) - 需要一个m*n的矩阵存储中间结果

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 获取矩阵的行数和列数
        m = len(grid)
        n = len(grid[0])
        
        # 创建dp数组,用于存储到达每个格子的最小路径和
        dp = [[0] * n for _ in range(m)]
        
        # 处理第一个格子
        dp[0][0] = grid[0][0]
        
        # 处理第一行
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
            
        # 处理第一列
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            
        # 处理其他格子
        for i in range(1, m):
            for j in range(1, n):
                # 当前格子的最小路径和等于上方格子和左方格子的最小路径和的较小值加上当前格子的值
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        # 返回右下角格子的最小路径和
        return dp[m-1][n-1]
        
# @lc code=end
