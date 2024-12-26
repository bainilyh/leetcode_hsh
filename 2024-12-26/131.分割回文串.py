# #
# # @lc app=leetcode.cn id=131 lang=python3
# #
# # [131] 分割回文串
# #
# # 解题思路:
# # 1. 使用回溯法(DFS)遍历所有可能的分割方案
# # 2. 对于每个子串判断是否为回文串
# # 3. 使用动态规划预处理判断子串是否为回文串,避免重复计算
# #
# # 数据结构:
# # - 列表(List): 存储结果和当前路径
# # - 二维数组: 存储子串是否为回文串的状态
# #
# # 算法:
# # - 回溯法(DFS)
# # - 动态规划
# #
# # 时间复杂度: O(n*2^n), n为字符串长度
# # 空间复杂度: O(n^2), 主要是dp数组的空间

# # @lc code=start
# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         n = len(s)
#         # dp[i][j]表示s[i:j+1]是否为回文串
#         dp = [[True] * n for _ in range(n)]
        
#         # 预处理所有子串是否为回文
#         for i in range(n-1, -1, -1):
#             for j in range(i+1, n):
#                 dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        
#         res = []  # 存储最终结果
#         path = []  # 存储当前路径
        
#         def backtrack(start):
#             # 如果起始位置已经到达字符串末尾,说明找到一个有效方案
#             if start >= n:
#                 res.append(path[:])
#                 return
            
#             # 枚举所有可能的结束位置
#             for end in range(start, n):
#                 # 如果当前子串是回文串,则进行递归
#                 if dp[start][end]:
#                     path.append(s[start:end + 1])
#                     backtrack(end + 1)
#                     path.pop()  # 回溯,恢复状态
        
#         backtrack(0)  # 从位置0开始回溯
#         return res

# # @lc code=end
