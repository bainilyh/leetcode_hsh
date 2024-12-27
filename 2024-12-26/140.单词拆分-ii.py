#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        解题思路:
        1. 使用记忆化递归解决问题
        2. 递归函数返回从当前位置到字符串末尾的所有可能拆分
        3. 使用记忆化避免重复计算子问题
        """
        word_set = set(wordDict)
        n = len(s)
        memo = {}

        def dfs(start):
            if start == n:
                return ['']
            if start in memo:
                return memo[start]

            res = []
            for end in range(start + 1, n + 1):
                word = s[start:end]
                if word in word_set:
                    sub_sentences = dfs(end)
                    for sub in sub_sentences:
                        res.append((word + ' ' + sub).strip())

            memo[start] = res
            return res

        return dfs(0)

# @lc code=end

# 数据结构:
# - 集合(set): 用于存储wordDict中的单词，提高查找效率
# - 字典(dict): 用于记忆化，存储中间结果
# - 递归调用栈: 用于深度优先搜索过程

# 算法:
# - 深度优先搜索(DFS): 生成所有可能的拆分结果
# - 记忆化: 避免重复计算子问题

# 时间复杂度: O(n^3)
# - 在最坏情况下，每个子问题只会被计算一次，共有n个子问题
# - 对于每个子问题，我们最多需要O(n)的时间来检查所有可能的拆分点
# - 字符串拼接操作需要O(n)的时间

# 空间复杂度: O(n^2)
# - 记忆化字典在最坏情况下需要存储O(n)个子问题的结果
# - 每个子问题的结果可能包含O(n)个字符串
# - 递归调用栈的深度为O(n)
