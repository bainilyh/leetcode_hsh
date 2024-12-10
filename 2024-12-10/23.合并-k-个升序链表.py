#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import List, Optional
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 解题思路：使用最小堆来合并K个有序链表
        # 数据结构：最小堆（优先队列）
        # 算法：堆排序

        # 创建一个最小堆
        min_heap = []
        
        # 将每个链表的头节点加入最小堆
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(min_heap, (lst.val, i, lst))
        
        # 创建一个哑节点作为合并后链表的头部
        dummy = ListNode(0)
        current = dummy
        
        # 不断从最小堆中取出最小元素，添加到结果链表中
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            
            # 如果取出的节点还有下一个节点，将其加入最小堆
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next

# @lc code=end

# 时间复杂度：O(N log k)，其中 N 是所有链表中元素的总数，k 是链表的数量。
# 每个元素都会被加入和取出堆一次，每次堆操作的时间复杂度为 O(log k)。

# 空间复杂度：O(k)，其中 k 是链表的数量。
# 最小堆中最多同时存在 k 个元素。
