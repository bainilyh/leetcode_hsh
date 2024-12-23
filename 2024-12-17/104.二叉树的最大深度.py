#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# 解题思路:
# 1. 使用递归方法计算二叉树的最大深度
# 2. 二叉树的最大深度等于左右子树的最大深度加1
# 3. 递归终止条件是节点为空,返回深度0
#
# 使用的数据结构和算法:
# - 数据结构: 二叉树
# - 算法: 递归、深度优先搜索(DFS)
#
# 时间复杂度: O(n), n为节点数,需要遍历所有节点
# 空间复杂度: O(h), h为树的高度,递归调用栈的深度

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 如果节点为空,返回深度0
        if not root:
            return 0
            
        # 递归计算左右子树的最大深度
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # 返回左右子树最大深度加1
        return max(left_depth, right_depth) + 1
        
# @lc code=end
