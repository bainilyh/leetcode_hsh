#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# 解题思路:
# 1. 使用递归的方法,从根节点开始,每次减去当前节点的值
# 2. 如果到达叶子节点时,剩余的targetSum为0,说明存在这样的路径
# 3. 如果到达叶子节点时,剩余的targetSum不为0,继续递归左右子树
#
# 使用的数据结构和算法:
# - 数据结构:二叉树
# - 算法:递归(深度优先搜索DFS)
#
# 时间复杂度:O(N),其中N是树的节点数,需要遍历所有节点
# 空间复杂度:O(H),其中H是树的高度,递归调用栈的空间

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 如果根节点为空,返回False
        if not root:
            return False
            
        # 如果是叶子节点,判断当前值是否等于目标和
        if not root.left and not root.right:
            return root.val == targetSum
            
        # 递归判断左右子树是否存在路径和为targetSum减去当前节点值的路径
        return self.hasPathSum(root.left, targetSum - root.val) or \
               self.hasPathSum(root.right, targetSum - root.val)
        
# @lc code=end
