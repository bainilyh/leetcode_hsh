#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 如果needle为空字符串，返回0
        if not needle:
            return 0
        
        # 获取haystack和needle的长度
        n, m = len(haystack), len(needle)
        
        # 遍历haystack字符串
        for i in range(n - m + 1):
            # 检查从i开始的子串是否与needle匹配
            if haystack[i:i+m] == needle:
                return i
        
        # 如果没有找到匹配，返回-1
        return -1

# @lc code=end

# 解题思路：
# 1. 遍历haystack字符串，检查每个可能的起始位置。
# 2. 对于每个起始位置，比较从该位置开始的子串是否与needle相等。
# 3. 如果找到匹配，返回起始索引；如果遍历完没有找到，返回-1。

# 数据结构：
# - 字符串：用于存储和比较haystack和needle。

# 算法：
# - 线性扫描：遍历haystack字符串。
# - 字符串切片和比较：用于检查子串是否匹配。

# 时间复杂度：O((n-m+1)*m)，其中n是haystack的长度，m是needle的长度。
# 最坏情况下，需要比较haystack的每个子串。

# 空间复杂度：O(1)，只使用了常数额外空间。
