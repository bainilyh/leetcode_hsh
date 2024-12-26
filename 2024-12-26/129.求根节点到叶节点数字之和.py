#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#
# 解题思路:
# 1. 使用深度优先搜索(DFS)遍历二叉树
# 2. 从根节点到叶节点形成一个数字,需要在遍历过程中记录当前路径的数字
# 3. 到达叶节点时,将该路径形成的数字加入总和
#
# 数据结构:
# - 二叉树
# 
# 算法:
# - 深度优先搜索(DFS)
#
# 时间复杂度: O(N) - N为节点数,需要访问每个节点一次
# 空间复杂度: O(H) - H为树的高度,递归调用栈的空间

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, current_num: int) -> int:
            # 如果节点为空,返回0
            if not node:
                return 0
            
            # 计算当前路径的数字
            current_num = current_num * 10 + node.val
            
            # 如果是叶节点,返回当前数字
            if not node.left and not node.right:
                return current_num
            
            # 递归处理左右子树,并返回它们的和
            return dfs(node.left, current_num) + dfs(node.right, current_num)
        
        # 从根节点开始DFS
        return dfs(root, 0)
        
# @lc code=end
