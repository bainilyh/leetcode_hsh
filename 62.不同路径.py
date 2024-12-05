#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
            路径问题不要扩充dp数组
        """
        # dp[i][j]表示到达当前位置有多少路径
        dp = [[1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # if i == 0 and j == 0:
                #     continue
                # dp[i][j] = 1
                # if i != 0:
                #     dp[i][j] += dp[i - 1][j]
                # if j != 0:
                #     dp[i][j] += dp[i][j - 1]
                if i != 0 and j != 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
        return dp[m - 1][n - 1]
        
# @lc code=end

