#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
# 解题思路:
# 1. 这是一个典型的动态规划问题
# 2. 机器人每次只能向右或向下移动,要到达终点的路径数等于到达上方格子的路径数加上到达左方格子的路径数
# 3. 使用二维数组dp[i][j]表示到达(i,j)位置的不同路径数
# 4. 第一行和第一列的格子只有一种到达方式
# 5. 其他格子的路径数为: dp[i][j] = dp[i-1][j] + dp[i][j-1]
#
# 数据结构: 二维数组(矩阵)
# 算法: 动态规划
#
# 时间复杂度: O(m*n) - 需要填充整个dp矩阵
# 空间复杂度: O(m*n) - 需要一个m*n的矩阵存储中间结果

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 创建m*n的二维数组,初始值都为1
        dp = [[1] * n for _ in range(m)]
        
        # 从第二行第二列开始填充数组
        for i in range(1, m):
            for j in range(1, n):
                # 当前格子的路径数等于上方格子的路径数加上左方格子的路径数
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # 返回右下角格子的路径数
        return dp[m-1][n-1]
        
# @lc code=end
