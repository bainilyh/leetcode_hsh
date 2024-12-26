#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#
# 解题思路:
# 1. 使用深度优先搜索(DFS)遍历原图的所有节点
# 2. 使用哈希表存储已克隆的节点,避免重复克隆
# 3. 对每个节点进行克隆,并递归克隆其邻居节点
#
# 使用的数据结构:
# - 哈希表(dict): 存储原节点到克隆节点的映射
# - 图的邻接表表示
#
# 算法: 深度优先搜索(DFS)

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # 特判: 如果输入节点为空,直接返回None
        if not node:
            return None
            
        # 创建哈希表用于存储已克隆的节点
        visited = {}
        
        def dfs(node):
            # 如果节点已被访问过,直接返回其克隆节点
            if node in visited:
                return visited[node]
                
            # 创建当前节点的克隆
            clone = Node(node.val)
            # 将原节点和克隆节点的对应关系存入哈希表
            visited[node] = clone
            
            # 递归克隆所有邻居节点
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            return clone
            
        # 从输入节点开始进行DFS克隆
        return dfs(node)

# 时间复杂度: O(N + M), 其中N是节点数,M是边数
# 空间复杂度: O(N), 主要是哈希表的开销
# @lc code=end
