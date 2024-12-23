#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# 解题思路:
# 1. 前序遍历的第一个节点是根节点
# 2. 在中序遍历中找到根节点的位置,可以将数组分成左右子树
# 3. 递归构建左右子树
# 4. 使用切片获取对应的子数组进行递归
#
# 使用的数据结构和算法:
# - 数据结构: 二叉树、数组
# - 算法: 递归、分治
#
# 时间复杂度: O(n), n为节点数,需要遍历所有节点
# 空间复杂度: O(n), 递归调用栈的深度为O(h),h为树的高度,最坏情况下h=n

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 如果序列为空,返回None
        if not preorder or not inorder:
            return None
            
        # 前序遍历的第一个节点是根节点
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # 在中序遍历中找到根节点的位置
        root_index = inorder.index(root_val)
        
        # 递归构建左子树
        # 左子树的前序遍历为preorder[1:root_index+1]
        # 左子树的中序遍历为inorder[:root_index]
        root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        
        # 递归构建右子树
        # 右子树的前序遍历为preorder[root_index+1:]
        # 右子树的中序遍历为inorder[root_index+1:]
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])
        
        return root
        
# @lc code=end
