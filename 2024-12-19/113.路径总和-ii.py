#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# 解题思路:
# 1. 使用深度优先搜索(DFS)遍历二叉树
# 2. 维护一个路径数组path记录从根节点到当前节点的路径
# 3. 当遍历到叶子节点时,判断路径和是否等于目标值
# 4. 如果相等则将当前路径加入结果集
#
# 使用的数据结构和算法:
# - 数据结构: 二叉树、列表(用于存储路径)
# - 算法: 深度优先搜索(DFS)、回溯
#
# 时间复杂度: O(N), N为二叉树节点数
# 空间复杂度: O(H), H为二叉树高度(递归调用栈的深度)

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # 存储所有满足条件的路径
        result = []
        
        def dfs(node: TreeNode, target: int, path: List[int]):
            # 如果节点为空,直接返回
            if not node:
                return
            
            # 将当前节点值加入路径
            path.append(node.val)
            
            # 如果是叶子节点且路径和等于目标值
            if not node.left and not node.right and target == node.val:
                # 将当前路径的副本加入结果集
                result.append(path[:])
            
            # 递归遍历左子树,目标值减去当前节点值
            dfs(node.left, target - node.val, path)
            # 递归遍历右子树,目标值减去当前节点值
            dfs(node.right, target - node.val, path)
            
            # 回溯,移除当前节点
            path.pop()
        
        # 从根节点开始DFS
        dfs(root, targetSum, [])
        return result

# @lc code=end
