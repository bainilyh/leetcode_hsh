# #
# # @lc app=leetcode.cn id=93 lang=python3
# #
# # [93] 复原 IP 地址
# #
# # 解题思路:
# # 1. 使用回溯法将字符串分成4个部分,每个部分代表IP地址的一段
# # 2. 每一段IP地址需要满足:
# #    - 长度在1-3之间
# #    - 如果长度>1,不能以0开头
# #    - 转换成数字后要在0-255之间
# # 3. 使用start记录当前处理的字符串位置,dots记录已添加的点数
# #
# # 数据结构:
# # - 字符串(String): 存储输入和中间结果
# # - 列表(List): 存储最终的IP地址结果
# #
# # 算法: 回溯法(Backtracking)

# # @lc code=start
# class Solution:
#     def restoreIpAddresses(self, s: str) -> List[str]:
#         # 定义结果列表
#         result = []
        
#         def backtrack(start: int, dots: int, curr: str):
#             # 如果已经添加了3个点,检查最后一段是否有效
#             if dots == 3:
#                 last_segment = s[start:]
#                 if is_valid_segment(last_segment):
#                     result.append(curr + last_segment)
#                 return
            
#             # 尝试在不同位置添加点
#             for i in range(start, min(start + 3, len(s))):
#                 segment = s[start:i + 1]
#                 if is_valid_segment(segment):
#                     backtrack(i + 1, dots + 1, curr + segment + '.')
        
#         def is_valid_segment(segment: str) -> bool:
#             # 空段无效
#             if not segment:
#                 return False
#             # 长度>1且以0开头无效
#             if len(segment) > 1 and segment[0] == '0':
#                 return False
#             # 长度>3无效
#             if len(segment) > 3:
#                 return False
#             # 转换成数字后需要在0-255之间
#             return 0 <= int(segment) <= 255
        
#         # 如果字符串长度不在合理范围内,直接返回空列表
#         if len(s) < 4 or len(s) > 12:
#             return []
            
#         # 从空字符串开始回溯
#         backtrack(0, 0, '')
#         return result

# # 时间复杂度: O(1) - 因为IP地址最多12位,所以是常数时间
# # 空间复杂度: O(1) - 递归深度最多为4,存储空间也是常数级别
# # @lc code=end
