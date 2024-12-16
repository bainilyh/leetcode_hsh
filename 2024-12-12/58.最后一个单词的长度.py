#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# 解题思路:
# 1. 先去除字符串末尾的空格
# 2. 从右向左遍历字符串,直到遇到第一个空格或到达字符串开头
# 3. 记录这个过程中遍历的字符数量即为最后一个单词的长度
#
# 使用的数据结构和算法:
# - 字符串处理
# - 从右向左遍历
#
# 时间复杂度: O(n), 其中n为字符串长度
# 空间复杂度: O(1), 只使用了常数额外空间

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 去除字符串末尾的空格
        s = s.rstrip()
        
        # 记录最后一个单词的长度
        length = 0
        
        # 从右向左遍历字符串
        for i in range(len(s)-1, -1, -1):
            # 如果遇到空格,说明已经找到最后一个单词
            if s[i] == ' ':
                break
            length += 1
            
        return length
        
# @lc code=end
