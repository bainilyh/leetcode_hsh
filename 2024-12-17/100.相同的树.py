#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#
# 解题思路:
# 1. 使用递归方法比较两棵二叉树是否相同
# 2. 两棵树相同的条件是:
#    - 根节点的值相同
#    - 左子树相同
#    - 右子树相同
# 3. 递归终止条件:
#    - 两个节点都为空时返回True
#    - 一个节点为空另一个不为空时返回False
#    - 两个节点值不相等时返回False
#
# 数据结构: 二叉树
# 算法: 递归、深度优先搜索

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 如果两个节点都为空,返回True
        if not p and not q:
            return True
        # 如果其中一个节点为空,返回False
        if not p or not q:
            return False
        # 如果两个节点的值不相等,返回False
        if p.val != q.val:
            return False
        # 递归比较左右子树
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 时间复杂度: O(min(n,m)), n和m分别为两棵树的节点数,需要遍历到较小的树的所有节点
# 空间复杂度: O(min(h1,h2)), h1和h2分别为两棵树的高度,递归调用栈的最大深度
# @lc code=end
