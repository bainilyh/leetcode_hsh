#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# 解题思路:
# 1. 使用递归的方式计算二叉树的最小深度
# 2. 对于每个节点,分别计算其左右子树的最小深度
# 3. 需要注意的特殊情况:
#    - 如果节点为空,返回0
#    - 如果节点只有左子树,返回左子树的最小深度+1
#    - 如果节点只有右子树,返回右子树的最小深度+1
#    - 如果节点同时有左右子树,返回左右子树最小深度的较小值+1
#
# 使用的数据结构和算法:
# - 二叉树
# - 递归
# - 深度优先搜索(DFS)
#
# 时间复杂度: O(n), 其中n为节点数,每个节点只会被访问一次
# 空间复杂度: O(h), 其中h为树的高度,递归调用栈的空间

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 如果根节点为空,返回0
        if not root:
            return 0
            
        # 如果左子树为空,返回右子树的最小深度+1
        if not root.left:
            return self.minDepth(root.right) + 1
            
        # 如果右子树为空,返回左子树的最小深度+1    
        if not root.right:
            return self.minDepth(root.left) + 1
            
        # 如果左右子树都不为空,返回左右子树最小深度的较小值+1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
# @lc code=end
