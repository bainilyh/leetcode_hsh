#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 如果输入列表为空，返回空字符串
        if not strs:
            return ""
        
        # 获取第一个字符串作为基准
        first = strs[0]
        
        # 遍历第一个字符串的每个字符
        for i in range(len(first)):
            # 与其他字符串进行比较
            for other in strs[1:]:
                # 如果当前索引超出其他字符串长度，或字符不匹配
                if i >= len(other) or other[i] != first[i]:
                    # 返回当前索引之前的子串
                    return first[:i]
        
        # 如果循环结束仍未返回，说明第一个字符串就是最长公共前缀
        return first

# @lc code=end

# 解题思路：
# 1. 选择第一个字符串作为基准，逐字符与其他字符串比较。
# 2. 如果发现不匹配或超出长度，立即返回当前的公共前缀。

# 数据结构：
# - 字符串：用于存储和比较前缀。
# - 列表：输入的字符串数组。

# 算法：
# - 线性扫描：遍历字符串和数组。

# 时间复杂度：O(S)，其中S是所有字符串中字符的总数。
# 最坏情况下，需要比较每个字符串的每个字符。

# 空间复杂度：O(1)，只使用了常数额外空间。
