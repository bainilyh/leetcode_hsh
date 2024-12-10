#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        # 定义罗马数字符号和对应的整数值
        symbols = [
            ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
        ]
        
        roman = []  # 用于存储罗马数字结果
        
        # 遍历符号列表
        for symbol, value in symbols:
            # 当前数字大于等于符号对应的值时
            while num >= value:
                num -= value  # 减去对应的值
                roman.append(symbol)  # 添加对应的罗马数字符号
        
        return "".join(roman)  # 将结果列表连接成字符串

# @lc code=end

"""
解题思路：
1. 使用贪心算法，从大到小遍历罗马数字符号及其对应的整数值。
2. 对于每个符号，尽可能多地使用它来表示当前的数字。
3. 重复这个过程，直到数字被完全转换为罗马数字。

时间复杂度：O(1)，因为罗马数字的符号数量是固定的，且每个整数最多需要遍历一遍符号列表。
空间复杂度：O(1)，使用的额外空间不依赖于输入的大小。
"""
