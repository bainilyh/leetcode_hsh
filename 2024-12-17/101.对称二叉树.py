#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# 解题思路:
# 1. 使用递归方法判断二叉树是否对称
# 2. 两个子树对称的条件是:
#    - 它们的根节点值相等
#    - 左子树的左子节点和右子树的右子节点对称
#    - 左子树的右子节点和右子树的左子节点对称
# 3. 递归比较左右子树是否对称
#
# 使用的数据结构和算法:
# - 数据结构: 二叉树
# - 算法: 递归
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 如果根节点为空,则认为是对称的
        if not root:
            return True
            
        # 定义递归函数,判断两个子树是否对称    
        def check(left: TreeNode, right: TreeNode) -> bool:
            # 如果两个节点都为空,则对称
            if not left and not right:
                return True
            # 如果只有一个节点为空,则不对称    
            if not left or not right:
                return False
            # 判断:
            # 1. 当前节点值是否相等
            # 2. left的左子树和right的右子树是否对称
            # 3. left的右子树和right的左子树是否对称
            return (left.val == right.val and 
                    check(left.left, right.right) and
                    check(left.right, right.left))
        
        # 从根节点的左右子树开始判断是否对称
        return check(root.left, root.right)
        
# @lc code=end
