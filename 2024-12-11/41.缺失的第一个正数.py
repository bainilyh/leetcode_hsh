#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# 解题思路:
# 1. 利用数组本身作为哈希表,将数字放到对应的位置上
# 2. 数组长度为n,那么缺失的第一个正数一定在[1,n+1]范围内
# 3. 遍历数组,将每个在[1,n]范围内的数x放到索引x-1的位置
# 4. 再次遍历,第一个不在对应位置的数字的位置+1就是答案
#
# 数据结构:
# - 数组: 原地修改实现哈希表的效果
#
# 算法:
# - 原地哈希: 利用数组索引和值的对应关系
# - 双重遍历: 第一次放置数字,第二次查找缺失值
#
# 时间复杂度: O(n), n为数组长度
# 空间复杂度: O(1), 只使用常数额外空间

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 第一次遍历,将数字放到正确的位置
        for i in range(n):
            # 当前数字在[1,n]范围内且不在正确位置时进行交换
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        # 第二次遍历,找到第一个不在正确位置的数字
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # 如果数组中1到n都存在,返回n+1
        return n + 1
        
# @lc code=end
