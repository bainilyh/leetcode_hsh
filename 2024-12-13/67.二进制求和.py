#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# 解题思路:
# 1. 从两个字符串的最后一位开始向前遍历
# 2. 按照二进制加法规则进行计算,记录进位
# 3. 最后如果还有进位,需要在最前面加1
#
# 数据结构:
# - 字符串: 存储二进制数
# - 列表: 存储计算结果
#
# 时间复杂度: O(max(m,n)), m和n为两个字符串的长度
# 空间复杂度: O(max(m,n)), 需要存储结果字符串

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 初始化结果列表和进位
        result = []
        carry = 0
        
        # 获取两个字符串的长度
        i = len(a) - 1
        j = len(b) - 1
        
        # 从后向前遍历两个字符串
        while i >= 0 or j >= 0 or carry:
            # 获取当前位的值
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            # 计算当前位的和与进位
            curr_sum = digit_a + digit_b + carry
            carry = curr_sum // 2
            curr_digit = curr_sum % 2
            
            # 将当前位添加到结果列表
            result.append(str(curr_digit))
            
            # 移动指针
            i -= 1
            j -= 1
        
        # 反转结果列表并转换为字符串
        return ''.join(result[::-1])

# @lc code=end
