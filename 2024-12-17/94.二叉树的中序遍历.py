#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# 解题思路:
# 1. 使用递归方法实现二叉树的中序遍历
# 2. 中序遍历顺序: 左子树 -> 根节点 -> 右子树
# 3. 递归终止条件是当前节点为空
#
# 数据结构:
# - 二叉树(Binary Tree): 存储数据
# - 列表(List): 存储遍历结果
#
# 算法: 
# - 递归法: 直接按照中序遍历顺序递归访问左子树、根节点、右子树

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 定义结果列表
        result = []
        
        def inorder(node):
            # 递归终止条件
            if not node:
                return
            
            # 递归遍历左子树
            inorder(node.left)
            # 访问根节点
            result.append(node.val)
            # 递归遍历右子树
            inorder(node.right)
            
        # 从根节点开始递归
        inorder(root)
        return result

# 时间复杂度: O(n) - 每个节点都需要访问一次
# 空间复杂度: O(h) - h为树的高度,递归调用栈的深度,最坏情况下为O(n)
# @lc code=end
