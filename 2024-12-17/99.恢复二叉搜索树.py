# #
# # @lc app=leetcode.cn id=99 lang=python3
# #
# # [99] 恢复二叉搜索树
# #
# # 解题思路:
# # 1. 二叉搜索树的中序遍历是递增序列
# # 2. 如果有两个节点被错误交换，中序遍历时会出现两处逆序
# # 3. 使用Morris中序遍历可以实现O(1)空间复杂度
# # 4. 找到这两个逆序点后交换它们的值即可恢复二叉搜索树

# # @lc code=start
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def recoverTree(self, root: Optional[TreeNode]) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         # 记录需要交换的两个节点
#         self.first = None
#         self.second = None
#         # 记录前一个节点
#         self.prev = None
        
#         def inorder(root):
#             if not root:
#                 return
#             # 遍历左子树
#             inorder(root.left)
            
#             # 如果前一个节点的值大于当前节点值，说明需要交换
#             if self.prev and self.prev.val > root.val:
#                 # 第一个错误节点是第一次逆序时较大的节点
#                 if not self.first:
#                     self.first = self.prev
#                 # 第二个错误节点是最后一次逆序时较小的节点
#                 self.second = root
#             # 更新前一个节点    
#             self.prev = root
            
#             # 遍历右子树
#             inorder(root.right)
            
#         # 中序遍历找到需要交换的节点
#         inorder(root)
#         # 交换两个节点的值
#         self.first.val, self.second.val = self.second.val, self.first.val

# # 时间复杂度: O(N), N为二叉树节点数，需要遍历所有节点
# # 空间复杂度: O(H), H为二叉树高度，递归调用栈的开销
# # @lc code=end
