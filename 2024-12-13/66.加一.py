#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# 解题思路:
# 1. 从数组最后一位开始向前遍历
# 2. 如果当前位小于9,直接加1返回
# 3. 如果当前位等于9,将其置为0,继续向前遍历
# 4. 如果遍历完整个数组都没有返回,说明需要在最前面加1
#
# 数据结构:
# - 数组: 存储整数的每一位
#
# 时间复杂度: O(n), n为数组长度
# 空间复杂度: O(1), 只使用常数额外空间

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 从最后一位开始向前遍历
        for i in range(len(digits)-1, -1, -1):
            # 如果当前位小于9
            if digits[i] < 9:
                # 当前位加1后返回
                digits[i] += 1
                return digits
            # 如果当前位等于9,将其置为0
            digits[i] = 0
        
        # 如果遍历完整个数组都没有返回
        # 说明需要在最前面加1(如:999 + 1 = 1000)
        return [1] + digits

# @lc code=end
