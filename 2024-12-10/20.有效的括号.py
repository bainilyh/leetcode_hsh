#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 使用栈来匹配括号
        stack = []
        # 定义括号匹配字典
        bracket_map = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in bracket_map:
                # 如果是右括号，检查栈顶元素是否匹配
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                # 如果是左括号，入栈
                stack.append(char)
        
        # 栈为空说明所有括号都匹配成功
        return len(stack) == 0

# @lc code=end

"""
解题思路：
1. 使用栈来存储左括号
2. 遍历字符串，遇到左括号就入栈
3. 遇到右括号就检查栈顶元素是否匹配，匹配则出栈，不匹配则返回False
4. 最后检查栈是否为空，为空则所有括号都匹配成功

数据结构：栈（使用Python的列表实现）
算法：遍历 + 栈操作

时间复杂度：O(n)，其中n是字符串的长度，需要遍历整个字符串一次
空间复杂度：O(n)，最坏情况下（所有字符都是左括号）需要将所有字符压入栈中
"""
