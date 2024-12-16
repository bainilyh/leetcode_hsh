#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# 解题思路:
# 1. 使用动态规划求解编辑距离
# 2. dp[i][j]表示word1的前i个字符转换到word2的前j个字符需要的最少操作数
# 3. 状态转移方程:
#    - 如果word1[i-1] == word2[j-1], dp[i][j] = dp[i-1][j-1]
#    - 否则, dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
#      分别对应删除、插入和替换操作
# 4. 初始化:
#    - dp[i][0] = i (删除i个字符)
#    - dp[0][j] = j (插入j个字符)
#
# 数据结构:
# - 二维数组: dp数组存储中间状态
#
# 时间复杂度: O(mn), m和n分别为两个字符串的长度
# 空间复杂度: O(mn), 需要二维dp数组

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 获取两个字符串的长度
        m, n = len(word1), len(word2)
        
        # 创建dp数组并初始化
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 初始化第一行和第一列
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
            
        # 填充dp数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果字符相同,不需要操作
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # 否则取删除、插入、替换三种操作的最小值
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        # 返回最终结果
        return dp[m][n]

# @lc code=end
