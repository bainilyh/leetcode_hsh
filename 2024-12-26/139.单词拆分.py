#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        解题思路:
        1. 使用记忆化递归来解决问题
        2. memo[i]表示s[:i]能否拆分成wordDict中的单词
        3. backtrack(i)表示s[i:]能否拆分成wordDict中的单词
        """
        #  memo[i]表示s[:i]能否拆分成wordDict中的单词
        memo = {}

        def backtrack(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]

            for j in range(i + 1, len(s) + 1):
                # 如果s[i:j]在wordDict中，并且backtrack(j)为True
                if s[i:j] in wordDict and backtrack(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return backtrack(0)


# @lc code=end

# 数据结构:
# - memo字典，用于存储每个子串能否拆分成wordDict中的单词

# 算法:
# - 记忆化递归

# 时间复杂度：O(n^2)
# 空间复杂度：O(n)
