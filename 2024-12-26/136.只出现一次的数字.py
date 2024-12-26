#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# 解题思路:
# 1. 使用异或运算的性质:
#    - 任何数和0异或等于它本身: a⊕0 = a
#    - 任何数和自己异或等于0: a⊕a = 0
#    - 异或运算满足交换律和结合律
# 2. 将所有数字进行异或运算,相同的数字会抵消为0
#    最后剩下的就是只出现一次的数字
# 
# 时间复杂度: O(n) - 需要遍历一遍数组
# 空间复杂度: O(1) - 只需要一个变量存储结果

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 初始化结果为0
        result = 0
        
        # 遍历数组中的每个数字
        for num in nums:
            # 将当前数字与结果进行异或运算
            result ^= num
            
        return result
        
# @lc code=end
