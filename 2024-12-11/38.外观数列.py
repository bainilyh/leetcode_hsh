#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#
# 解题思路:
# 1. 从n=1开始,递归生成每一项的外观数列
# 2. 对于每一项,使用双指针遍历字符串,统计连续相同数字的个数
# 3. 根据统计结果拼接得到下一项
#
# 数据结构:
# - 字符串: 存储每一项的结果
# - 双指针: 用于统计连续相同数字
#
# 算法:
# - 递归: 从n=1开始,递归生成每一项
# - 双指针: 统计连续相同数字的个数
#
# 时间复杂度: O(n*m), n为给定数字,m为生成的字符串的平均长度
# 空间复杂度: O(m), m为生成的字符串的最大长度

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        # 基础情况,n=1时返回"1"
        if n == 1:
            return "1"
        
        # 递归获取上一项的结果
        prev = self.countAndSay(n-1)
        
        # 初始化结果字符串和指针
        result = ""
        i = 0
        
        # 遍历上一项字符串
        while i < len(prev):
            # 计数器初始化为1
            count = 1
            # 统计连续相同数字的个数
            while i + 1 < len(prev) and prev[i] == prev[i+1]:
                count += 1
                i += 1
            # 拼接当前数字的个数和数字本身
            result += str(count) + prev[i]
            i += 1
            
        return result
        
# @lc code=end
