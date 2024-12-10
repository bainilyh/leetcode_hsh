#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 获取字符串s和模式p的长度
        m, n = len(s), len(p)
        # 创建(m+1)x(n+1)的二维布尔数组dp，初始化为False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # 设置dp[0][0]为True，表示空字符串匹配空模式
        dp[0][0] = True
        
        # 处理模式p以'*'开头的特殊情况
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # 双重循环填充dp数组
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # 处理'*'的情况：可以匹配0次或多次
                    dp[i][j] = dp[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]
                elif p[j - 1] == '.' or s[i - 1] == p[j - 1]:
                    # 处理'.'或字符相等的情况
                    dp[i][j] = dp[i - 1][j - 1]
        
        # 返回最终结果dp[m][n]
        return dp[m][n]

# @lc code=end

# 数据结构：二维动态规划数组
# 算法：动态规划

# 时间复杂度：O(mn)，其中m和n分别是字符串s和模式p的长度。
# 需要填充大小为(m+1)x(n+1)的dp数组。

# 空间复杂度：O(mn)，需要一个(m+1)x(n+1)的二维数组来存储中间状态。
