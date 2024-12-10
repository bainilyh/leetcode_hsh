#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 初始化栈，存储括号的索引，初始放入-1作为哨兵
        stack = [-1]
        max_length = 0

        for i, char in enumerate(s):
            if char == '(':
                # 遇到左括号，将其索引入栈
                stack.append(i)
            else:
                # 遇到右括号，弹出栈顶元素
                stack.pop()
                if not stack:
                    # 栈为空，说明当前右括号没有匹配的左括号，将其索引入栈
                    stack.append(i)
                else:
                    # 计算当前有效括号串的长度
                    current_length = i - stack[-1]
                    # 更新最大长度
                    max_length = max(max_length, current_length)

        return max_length

# @lc code=end

"""
)()())
(()
解题思路：
1. 使用栈来匹配括号，栈中存储的是括号的索引
2. 遍历字符串，遇到左括号入栈，遇到右括号时尝试匹配
3. 通过计算匹配的括号之间的距离来得到有效括号子串的长度

数据结构：栈（使用Python的列表实现）
算法：一次遍历 + 栈操作

时间复杂度：O(n)，其中n是字符串的长度，只需要遍历一次字符串
空间复杂度：O(n)，最坏情况下（字符串中全是左括号）栈的大小为n
"""
