#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
# 解题思路:
# 1. 使用快速幂算法(分治)来计算x的n次方
# 2. 将n转换为二进制,根据二进制位为1的位置计算结果
# 3. 处理n为负数的情况
#
# 数据结构: 无特殊数据结构
# 算法: 快速幂算法(二分思想)
#
# 时间复杂度: O(logn) - 每次将n减半
# 空间复杂度: O(1) - 只使用常数额外空间

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 处理n为负数的情况
        if n < 0:
            x = 1/x
            n = -n
            
        # 初始化结果为1
        result = 1
        # 当前的x值
        current = x
        
        # 当n不为0时继续循环
        while n > 0: 
            # 如果n的二进制位最后一位为1
            if n & 1:
                # 将当前x值乘到结果中
                result *= current
            # 将当前x值平方
            current *= current
            # n右移一位
            n >>= 1
            
        return result
        
# @lc code=end
