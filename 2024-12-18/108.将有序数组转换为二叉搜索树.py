#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#
# 解题思路:
# 1. 由于要构造高度平衡的BST，我们需要选择有序数组的中间元素作为根节点
# 2. 将数组分成左右两部分，分别递归构造左右子树
# 3. 使用二分法+递归的思想解决
#
# 使用的数据结构和算法:
# - 数据结构：二叉搜索树（BST）
# - 算法：递归、二分查找
#
# 时间复杂度：O(n) - 每个节点被访问一次
# 空间复杂度：O(log n) - 递归调用栈的深度

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 如果数组为空，返回None
        if not nums:
            return None
            
        # 找到数组的中间位置
        mid = len(nums) // 2
        
        # 创建根节点，值为中间元素
        root = TreeNode(nums[mid])
        
        # 递归构造左子树，使用mid左边的元素
        root.left = self.sortedArrayToBST(nums[:mid])
        
        # 递归构造右子树，使用mid右边的元素
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return root
        
# @lc code=end
