#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# 解题思路:
# 1. 模拟竖式乘法的过程,从右往左遍历num2的每一位,与num1相乘
# 2. 将每次相乘的结果错位相加得到最终结果
# 3. 使用数组存储每位的结果,最后转换为字符串
#
# 数据结构:
# - 数组: 存储每位的计算结果
# - 字符串: 输入的两个数字字符串
#
# 算法:
# - 双重循环遍历两个数字的每一位进行相乘
# - 处理进位并将结果存入数组对应位置
# - 最后将数组转换为字符串,去除前导零

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 处理特殊情况
        if num1 == "0" or num2 == "0":
            return "0"
        
        # 初始化结果数组,长度为两数字长度之和
        res = [0] * (len(num1) + len(num2))
        
        # 从右往左遍历num1
        for i in range(len(num1)-1, -1, -1):
            # 从右往左遍历num2
            for j in range(len(num2)-1, -1, -1):
                # 当前位置的乘积
                mul = int(num1[i]) * int(num2[j])
                # 当前位置的和(包含之前的结果)
                p1 = i + j
                p2 = i + j + 1
                total = mul + res[p2]
                
                # 更新当前位和进位
                res[p2] = total % 10
                res[p1] += total // 10
        
        # 将数组转换为字符串,去除前导零
        result = ""
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        while i < len(res):
            result += str(res[i])
            i += 1
            
        return result if result else "0"

# @lc code=end

# 时间复杂度: O(m*n), 其中m和n分别是num1和num2的长度
# 空间复杂度: O(m+n), 需要一个长度为m+n的数组存储结果
