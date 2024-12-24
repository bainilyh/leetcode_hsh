#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# 解题思路:
# 1. 使用哈希集合存储所有数字,便于O(1)时间查找
# 2. 遍历数组中的每个数字x,如果x-1不在集合中,说明x是一个连续序列的起点
# 3. 从x开始向后查找x+1,x+2等数字是否在集合中,记录最长的连续序列长度
#
# 使用的数据结构和算法:
# - 数据结构:哈希集合(HashSet)
# - 算法:哈希表查找
#
# 时间复杂度:O(n) - 虽然有两层循环,但内层循环最多执行n次
# 空间复杂度:O(n) - 需要哈希集合存储所有数字

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 如果数组为空,返回0
        if not nums:
            return 0
            
        # 创建哈希集合,存储所有数字
        num_set = set(nums)
        max_length = 0
        
        # 遍历数组中的每个数字
        for num in num_set:
            # 如果num-1不在集合中,说明num是一个连续序列的起点
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                # 向后查找连续的数字
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                    
                # 更新最长连续序列的长度
                max_length = max(max_length, current_length)
                
        return max_length
        
# @lc code=end
