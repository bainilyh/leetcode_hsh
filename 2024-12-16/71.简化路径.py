#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#
# 解题思路:
# 1. 使用栈来处理路径
# 2. 先将路径按'/'分割成多个部分
# 3. 遍历每个部分:
#    - 如果是'.'或空,跳过
#    - 如果是'..',弹出栈顶元素(如果栈不为空)
#    - 其他情况,将当前部分压入栈
# 4. 最后将栈中元素用'/'连接
#
# 数据结构:
# - 栈: 存储有效的路径部分
# - 字符串: 存储路径
#
# 时间复杂度: O(n), n为路径长度
# 空间复杂度: O(n), 需要栈存储路径部分

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        # 初始化栈
        stack = []
        
        # 将路径按'/'分割
        parts = path.split('/')
        
        # 遍历每个部分
        for part in parts:
            # 如果是'..'且栈不为空,弹出栈顶
            if part == '..' and stack:
                stack.pop()
            # 如果不是特殊字符且不为空,压入栈
            elif part and part != '.' and part != '..':
                stack.append(part)
        
        # 返回简化后的路径
        return '/' + '/'.join(stack)

# @lc code=end
