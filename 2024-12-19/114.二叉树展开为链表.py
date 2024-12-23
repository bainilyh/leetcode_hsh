#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        # 将左子树和右子树展开
        self.flatten(root.left)
        self.flatten(root.right)
        
        # 保存右子树
        right = root.right
        
        # 将左子树移到右子树位置
        root.right = root.left
        root.left = None
        
        # 将右子树连接到当前右子树的末尾
        while root.right:
            root = root.right
        root.right = right
        
# @lc code=end

