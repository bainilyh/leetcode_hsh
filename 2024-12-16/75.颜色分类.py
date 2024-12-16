#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
# 解题思路:
# 使用双指针法,将数组分成三个区域:
# 左边全是0,中间全是1,右边全是2
# 使用两个指针p0和p2分别指向0的右边界和2的左边界
# 使用一个遍历指针i从左向右遍历
# 如果遇到0就和p0交换,遇到2就和p2交换
# 遇到1就继续遍历

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 定义双指针,p0指向0的右边界,p2指向2的左边界
        p0 = 0  
        p2 = len(nums) - 1
        i = 0
        
        # 当遍历指针不超过p2时继续遍历
        while i <= p2:
            # 如果当前数是0,就和p0交换,并将p0和i都右移
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            # 如果当前数是2,就和p2交换,并将p2左移
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            # 如果当前数是1,继续遍历
            else:
                i += 1

# 时间复杂度:O(n),只需要遍历一遍数组
# 空间复杂度:O(1),只使用了常数个变量
# @lc code=end
