#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 解题思路：排序 + 双指针
        # 数据结构：列表
        # 算法：排序，嵌套循环 + 双指针

        nums.sort()  # 对数组进行排序
        n = len(nums)
        result = []

        for a in range(n - 3):  # 固定第一个数
            if a > 0 and nums[a] == nums[a - 1]:
                continue  # 跳过重复的第一个数

            for b in range(a + 1, n - 2):  # 固定第二个数
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue  # 跳过重复的第二个数

                c, d = b + 1, n - 1  # 设置双指针

                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]

                    if total == target:
                        result.append([nums[a], nums[b], nums[c], nums[d]])
                        
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1  # 跳过重复的第三个数
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1  # 跳过重复的第四个数
                        
                        c += 1
                        d -= 1
                    elif total < target:
                        c += 1  # 和小于目标值，左指针右移
                    else:
                        d -= 1  # 和大于目标值，右指针左移

        return result

# @lc code=end

# 时间复杂度：O(n^3)，其中 n 是数组的长度。排序的时间复杂度是 O(nlogn)，
# 两层嵌套循环 + 双指针遍历的时间复杂度是 O(n^3)，总体时间复杂度为 O(n^3)。
# 空间复杂度：O(1)，除了存储答案的列表外，我们只需要常数级别的空间。
