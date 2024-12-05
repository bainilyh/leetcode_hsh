#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
# 1, 0, 0, 1
# 0, 1, 1, 0
# 0, 1, 1, 1
# 1, 0, 1, 1
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # def dfs(isConnected, i, j):
        #     if i < 0 or j < 0 or i >= len(isConnected) or j >= len(isConnected[0]):
        #         return 0
        #     if isConnected[i][j] == 0:
        #         return 0
            
        #     isConnected[i][j] = 0
        #     dfs(isConnected, i - 1, j)
        #     dfs(isConnected, i + 1, j)
        #     dfs(isConnected, i, j - 1)
        #     dfs(isConnected, i, j + 1)
        #     return 1
        # res = 0
        # for i in range(len(isConnected)):
        #     for j in range(len(isConnected[0])):
        #         res += dfs(isConnected, i, j)
        # return res
    
# @lc code=end

