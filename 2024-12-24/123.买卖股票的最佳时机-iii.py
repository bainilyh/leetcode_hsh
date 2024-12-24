# #
# # @lc app=leetcode.cn id=123 lang=python3
# #
# # [123] 买卖股票的最佳时机 III
# #
# # 解题思路:
# # 1. 使用动态规划,dp[i][k][j]表示第i天,已进行k次交易,状态为j时的最大利润
# # 2. j的取值为0-1,分别表示:
# #    0:不持有股票
# #    1:持有股票
# # 3. k的取值为0-2,表示已完成的交易次数
# # 4. 状态转移方程:
# #    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
# #    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
# #
# # 使用的数据结构和算法:
# # - 数据结构:三维dp数组
# # - 算法:动态规划
# #
# # 时间复杂度:O(n) - 需要遍历一次价格数组
# # 空间复杂度:O(n) - 需要n*3*2的dp数组,可以优化到O(1)

# # @lc code=start
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # 如果价格列表为空或只有一天，无法获得利润
#         if len(prices) <= 1:
#             return 0
            
#         n = len(prices)
#         # 创建dp数组,大小为n*3*2
#         dp = [[[0] * 2 for _ in range(3)] for _ in range(n)]
        
#         # 初始化第一天的状态
#         for k in range(3):
#             dp[0][k][0] = 0  # 第一天不持有股票
#             dp[0][k][1] = -prices[0]  # 第一天持有股票
        
#         # 遍历每一天
#         for i in range(1, n):
#             for k in range(3):  # k表示已完成的交易次数,最多2次
#                 if k == 0:
#                     # 如果还没有交易,只能保持不变或买入
#                     dp[i][k][0] = dp[i-1][k][0]
#                     dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])
#                 else:
#                     # 可以选择保持不变或进行交易
#                     dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
#                     dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
            
#         # 返回最后一天完成2次交易且不持有股票的状态(最大利润)
#         return dp[n-1][2][0]
        
# # @lc code=end
