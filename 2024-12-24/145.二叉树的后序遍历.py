# #
# # @lc app=leetcode.cn id=145 lang=python3
# #
# # [145] 二叉树的后序遍历
# #
# # 解题思路:
# # 1. 后序遍历的顺序是: 左子树 -> 右子树 -> 根节点
# # 2. 可以使用递归或迭代的方式实现
# # 3. 这里使用递归方式，将遍历结果存储在列表中返回
# #
# # 数据结构: 二叉树
# # 算法: 递归/深度优先搜索(DFS)
# #
# # 时间复杂度: O(n), n为节点数量，需要访问每个节点一次
# # 空间复杂度: O(h), h为树的高度，递归调用栈的最大深度

# # @lc code=start
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         # 存储遍历结果的列表
#         result = []
        
#         def dfs(node):
#             # 如果节点为空，直接返回
#             if not node:
#                 return
#             # 递归遍历左子树
#             dfs(node.left)
#             # 递归遍历右子树 
#             dfs(node.right)
#             # 将当前节点值加入结果列表
#             result.append(node.val)
        
#         # 从根节点开始遍历
#         dfs(root)
#         return result
        
# # @lc code=end
