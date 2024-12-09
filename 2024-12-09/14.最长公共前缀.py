#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n, m = len(strs[0]), len(strs)
        left = 0
        for i in range(n):
            for j in range(1, m):
                if len(strs[j]) > n or len(strs[j - 1]) > n or strs[j][i] != strs[j - 1][i]:
                    return strs[0][:left]
            left += 1
        return strs[0]
                
# @lc code=end

