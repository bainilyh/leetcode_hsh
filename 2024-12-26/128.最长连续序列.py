#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# 解题思路:
# 1. 使用哈希集合存储所有数字,实现O(1)查找
# 2. 遍历数组,对每个数字x,如果x-1不在集合中,说明x是序列的起点
# 3. 从x开始向后查找连续的数字,更新最大长度
#
# 数据结构: 哈希集合(HashSet)
# 算法: 哈希表 + 线性遍历
#
# 时间复杂度: O(n) - 遍历数组一次,每个数字最多被访问两次
# 空间复杂度: O(n) - 需要哈希集合存储所有数字

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 创建哈希集合存储所有数字
        num_set = set(nums)
        # 记录最长连续序列的长度
        longest_streak = 0
        
        # 遍历数组中的每个数字
        for num in num_set:
            # 如果num-1不在集合中,说明num是序列的起点
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # 从num开始向后查找连续的数字
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                # 更新最长连续序列的长度
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
        
# @lc code=end
