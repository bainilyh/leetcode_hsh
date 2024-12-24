#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#
# 解题思路:
# 1. 将字符串转换为小写,并过滤出字母和数字字符
# 2. 使用双指针从两端向中间移动比较字符是否相同
# 
# 数据结构:
# - 字符串
# - 双指针
#
# 算法:
# - 双指针法
#
# 时间复杂度: O(n), n为字符串长度
# 空间复杂度: O(1), 只使用了常数额外空间

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 将字符串转换为小写
        s = s.lower()
        
        # 双指针初始化在字符串两端
        left, right = 0, len(s) - 1
        
        while left < right:
            # 跳过非字母数字字符
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
                
            # 比较两端字符是否相同
            if s[left] != s[right]:
                return False
                
            # 指针向中间移动
            left += 1
            right -= 1
            
        return True
        
# @lc code=end
