#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# 解题思路:
# 1. 由于nums1后面有足够空间,可以从后往前比较两个数组的元素,将较大的放入nums1末尾
# 2. 使用三个指针:p1指向nums1有效元素末尾,p2指向nums2末尾,p指向nums1数组末尾
# 3. 比较p1和p2指向的元素大小,将较大的放入p位置,并将对应指针前移
# 4. 当p2<0时结束,如果p1>=0的元素都已在正确位置,如果p2>=0需要将nums2剩余元素复制到nums1前面
#
# 数据结构: 数组
# 算法: 双指针

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 初始化三个指针
        p1 = m - 1  # nums1有效元素末尾
        p2 = n - 1  # nums2末尾
        p = m + n - 1  # nums1数组末尾
        
        # 从后向前遍历
        while p2 >= 0:  # nums2还有元素未合并
            if p1 >= 0 and nums1[p1] > nums2[p2]:  # nums1当前元素更大
                nums1[p] = nums1[p1]  # 放入nums1末尾
                p1 -= 1  # p1左移
            else:  # nums2当前元素更大或nums1已处理完
                nums1[p] = nums2[p2]  # 放入nums1末尾
                p2 -= 1  # p2左移
            p -= 1  # p左移
            
# 时间复杂度: O(m+n) - 需要遍历两个数组的所有元素
# 空间复杂度: O(1) - 只使用了常数个额外变量
# @lc code=end
