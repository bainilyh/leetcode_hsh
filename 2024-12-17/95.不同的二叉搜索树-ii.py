# #
# # @lc app=leetcode.cn id=95 lang=python3
# #
# # [95] 不同的二叉搜索树 II
# #
# # 解题思路:
# # 1. 使用分治法和递归来生成所有可能的二叉搜索树
# # 2. 对于给定范围[start,end]内的每个值i，将其作为根节点
# # 3. 递归生成左子树(包含[start,i-1]范围内的值)和右子树(包含[i+1,end]范围内的值)
# # 4. 将所有可能的左右子树组合起来，形成不同的二叉搜索树
# #
# # 数据结构: 二叉树
# # 算法: 分治法、递归
# #
# # 时间复杂度: O(n * Cn)，其中Cn为第n个卡特兰数
# # 空间复杂度: O(n * Cn)，用于存储所有可能的二叉搜索树

# # @lc code=start
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
#         # 如果n为0，返回空列表
#         if n == 0:
#             return []
        
#         def generateSubtrees(start: int, end: int) -> List[Optional[TreeNode]]:
#             # 如果start大于end，返回只包含None的列表
#             if start > end:
#                 return [None]
            
#             all_trees = []
#             # 遍历start到end之间的每个数字作为根节点
#             for i in range(start, end + 1):
#                 # 递归生成所有可能的左子树
#                 left_trees = generateSubtrees(start, i - 1)
#                 # 递归生成所有可能的右子树
#                 right_trees = generateSubtrees(i + 1, end)
                
#                 # 组合所有可能的左右子树
#                 for left in left_trees:
#                     for right in right_trees:
#                         # 创建当前根节点
#                         root = TreeNode(i)
#                         root.left = left
#                         root.right = right
#                         all_trees.append(root)
            
#             return all_trees
        
#         # 从1到n生成所有可能的二叉搜索树
#         return generateSubtrees(1, n)

# # @lc code=end
