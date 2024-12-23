#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# 解题思路:
# 1. 使用动态规划数组dp，dp[i]表示到第i天为止的最大利润
# 2. 对于每一天，计算当前价格与前面最低价格的差值
# 3. dp[i] = max(dp[i-1], prices[i] - min_price)
#
# 使用的数据结构和算法:
# - 使用动态规划数组dp记录每天的最大利润
# - 使用min_price记录到当前为止的最低价格
#
# 时间复杂度: O(n) - 需要遍历一次数组
# 空间复杂度: O(n) - 需要一个长度为n的dp数组

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 如果价格列表为空或只有一天，无法获得利润
        if len(prices) <= 1:
            return 0
            
        n = len(prices)
        # 创建dp数组，初始化为0
        dp = [0] * n
        # 初始化最小价格为第一天的价格
        min_price = prices[0]
        
        # 从第二天开始遍历
        for i in range(1, n):
            # 更新最小价格
            min_price = min(min_price, prices[i])
            # dp[i]为前一天的最大利润和当天价格减去最小价格中的较大值
            dp[i] = max(dp[i-1], prices[i] - min_price)
            
        # 返回最后一天的最大利润
        return dp[-1]
        
# @lc code=end
