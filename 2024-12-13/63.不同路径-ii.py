#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
# 解题思路:
# 1. 这是一个动态规划问题,与不同路径I类似,但需要考虑障碍物
# 2. 如果某个格子有障碍物,则该格子的路径数为0
# 3. 对于第一行和第一列,如果遇到障碍物,则后面的格子都无法到达
# 4. 对于其他格子,如果没有障碍物,则路径数等于上方格子和左方格子的路径数之和
#
# 数据结构: 二维数组(矩阵)
# 算法: 动态规划
#
# 时间复杂度: O(m*n) - 需要遍历整个矩阵
# 空间复杂度: O(m*n) - 需要一个m*n的矩阵存储中间结果

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 获取矩阵的行数和列数
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # 创建dp数组,用于存储到达每个格子的路径数
        dp = [[0] * n for _ in range(m)]
        
        # 处理第一个格子
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        # 处理第一行
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
                
        # 处理第一列
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
                
        # 处理其他格子
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # 返回右下角格子的路径数
        return dp[m-1][n-1]
        
# @lc code=end
