#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        """
            有效括号有两个关键点：
                1. 左右括号数量相等
                2. 字符串的某个前缀一定是左括号数量>=右括号数量
        """
        m = {')': '(', ']': '[', '}': '{'}
        stack = []
        for s_ in s:
            if s_ == '(' or s_ == '[' or s_ == '{':
                stack.append(s_)
            else:
                if not stack:
                    return False
                elif s_ in m and m[s_] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return not stack
    
# @lc code=end

