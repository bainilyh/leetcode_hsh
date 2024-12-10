#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # 定义罗马数字符号和对应的整数值
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        result = 0
        prev_value = 0
        
        # 从右向左遍历罗马数字字符串
        for char in s[::-1]:
            current_value = roman_values[char]
            
            # 如果当前值小于前一个值，说明是特殊情况（如IV），需要减去当前值
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value
            
            # 更新前一个值
            prev_value = current_value
        
        return result

# @lc code=end

"""
解题思路：
1. 创建一个字典，存储罗马数字符号及其对应的整数值。
2. 从右向左遍历罗马数字字符串，这样可以更容易处理特殊情况（如IV、IX等）。
3. 对于每个字符，获取其对应的整数值。
4. 如果当前值小于前一个值，说明遇到了特殊情况，需要减去当前值；否则加上当前值。
5. 更新前一个值，继续遍历。
6. 遍历结束后，返回累加的结果。

时间复杂度：O(n)，其中n是输入字符串的长度。我们只需要遍历一次字符串。
空间复杂度：O(1)，使用的额外空间（roman_values字典）是固定的，不随输入规模变化。
"""
