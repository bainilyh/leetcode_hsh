#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# 解题思路:
# 1. 使用递归的方式自底向上判断每个节点是否平衡
# 2. 对于每个节点,计算其左右子树的高度差,如果大于1则不平衡
# 3. 使用-1作为标记,表示子树不平衡
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 判断是否为平衡二叉树
        return self.height(root) >= 0
    
    def height(self, root: Optional[TreeNode]) -> int:
        # 如果节点为空,返回0
        if not root:
            return 0
        
        # 递归计算左子树高度
        left_height = self.height(root.left)
        # 如果左子树不平衡,返回-1
        if left_height == -1:
            return -1
            
        # 递归计算右子树高度    
        right_height = self.height(root.right)
        # 如果右子树不平衡,返回-1
        if right_height == -1:
            return -1
        
        # 判断当前节点是否平衡
        # 如果左右子树高度差大于1,返回-1表示不平衡
        if abs(left_height - right_height) > 1:
            return -1
            
        # 返回当前节点为根的子树高度
        return max(left_height, right_height) + 1
        
# @lc code=end
