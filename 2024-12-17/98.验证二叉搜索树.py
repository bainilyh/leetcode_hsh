#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# 解题思路:
# 1. 使用递归方法验证二叉搜索树
# 2. 对于每个节点,需要判断其值是否在合法范围内(min_val, max_val)
# 3. 左子树的所有节点值必须小于当前节点值,右子树的所有节点值必须大于当前节点值
# 4. 使用辅助函数validate()递归判断每个节点是否满足BST性质
#
# 数据结构: 二叉树
# 算法: 递归, 深度优先搜索
#
# 时间复杂度: O(n), n为节点数,需要访问每个节点一次
# 空间复杂度: O(h), h为树的高度,递归调用栈的最大深度

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: TreeNode, min_val: float, max_val: float) -> bool:
            # 空节点认为是合法的BST
            if not node:
                return True
            
            # 判断当前节点值是否在合法范围内
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # 递归验证左右子树
            # 左子树的所有节点值必须小于当前节点值
            # 右子树的所有节点值必须大于当前节点值
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
        
        # 初始调用时使用负无穷到正无穷的范围
        return validate(root, float('-inf'), float('inf'))

# @lc code=end
