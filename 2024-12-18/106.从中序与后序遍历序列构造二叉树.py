#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
解题思路:
1. 后序遍历的最后一个节点是根节点
2. 在中序遍历中找到根节点的位置，左边是左子树的中序遍历，右边是右子树的中序遍历
3. 根据中序遍历确定左右子树的大小，可以在后序遍历中划分出左右子树的后序遍历
4. 递归构建左右子树

使用的数据结构和算法:
- 二叉树
- 递归
- 哈希表(用于快速查找根节点在中序遍历中的位置)
"""

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 创建哈希表存储中序遍历的值到索引的映射
        self.index_map = {val: i for i, val in enumerate(inorder)}
        self.postorder = postorder
        self.inorder = inorder
        
        def helper(left: int, right: int, post_start: int, post_end: int) -> Optional[TreeNode]:
            # 如果左边界大于右边界，说明没有节点了
            if left > right:
                return None
                
            # 后序遍历的最后一个节点是根节点
            root_val = self.postorder[post_end]
            root = TreeNode(root_val)
            
            # 在中序遍历中找到根节点的位置
            root_index = self.index_map[root_val]
            
            # 计算左子树的节点数
            left_size = root_index - left
            
            # 递归构建左右子树
            root.left = helper(left, root_index - 1, post_start, post_start + left_size - 1)
            root.right = helper(root_index + 1, right, post_start + left_size, post_end - 1)
            
            return root
            
        n = len(inorder)
        return helper(0, n - 1, 0, n - 1)

"""
时间复杂度: O(n)，其中n是树中节点的数量
- 需要遍历每个节点一次来构建树
- 使用哈希表使得查找根节点在中序遍历中的位置的时间复杂度为O(1)

空间复杂度: O(n)
- 哈希表需要O(n)的空间
- 递归调用栈的深度最坏情况下为O(n)（当树完全倾斜时）
"""

# @lc code=end
