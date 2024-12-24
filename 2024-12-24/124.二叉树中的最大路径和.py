#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# 解题思路:
# 1. 使用递归的方式遍历二叉树,对于每个节点计算经过该节点的最大路径和
# 2. 对于每个节点,最大路径和可能有以下几种情况:
#    - 只包含当前节点
#    - 当前节点 + 左子树的最大路径
#    - 当前节点 + 右子树的最大路径
#    - 当前节点 + 左子树的最大路径 + 右子树的最大路径
# 3. 使用一个全局变量记录遍历过程中的最大路径和
#
# 数据结构: 二叉树
# 算法: 深度优先搜索(DFS)、递归
#
# 时间复杂度: O(N), N为二叉树节点数,需要遍历每个节点一次
# 空间复杂度: O(H), H为二叉树高度,递归调用栈的空间

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 初始化最大路径和为负无穷
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
                
            # 递归计算左右子树的最大贡献值
            # 只有在最大贡献值大于0时,才会选取对应子树
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # 节点的最大路径和取决于该节点的值与左右子树的最大贡献值
            price_newpath = node.val + left_gain + right_gain
            
            # 更新全局最大路径和
            self.max_sum = max(self.max_sum, price_newpath)
            
            # 返回节点的最大贡献值
            return node.val + max(left_gain, right_gain)
            
        max_gain(root)
        return self.max_sum

# @lc code=end
