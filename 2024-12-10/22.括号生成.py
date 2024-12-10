#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open_count, close_count):
            # 如果当前字符串长度等于2n，说明生成了一个有效的括号组合
            if len(trace) == 2 * n:
                result.append(''.join(trace))
                return
            
            # 如果开括号数量小于n，可以添加开括号
            if open_count < n:
                trace.append('(')
                backtrack(open_count + 1, close_count)
                trace.pop()
            
            # 如果闭括号数量小于开括号数量，可以添加闭括号
            if close_count < open_count:
                trace.append(')')
                backtrack(open_count, close_count + 1)
                trace.pop()

        result = []
        # 可以使用字符串,就不需要append和pop了.
        trace = [] 
        backtrack(0, 0)
        return result

# @lc code=end

"""
解题思路：
1. 使用回溯算法生成所有可能的括号组合
2. 在生成过程中保证括号的有效性：
   - 开括号数量不能超过n
   - 闭括号数量不能超过开括号数量

数据结构：
- 字符串：用于构建括号组合
- 列表：存储最终的有效括号组合

算法：回溯（深度优先搜索）

时间复杂度：O(4^n / sqrt(n))，卡特兰数的渐近复杂度
空间复杂度：O(n)，递归调用栈的深度最多为2n
"""
