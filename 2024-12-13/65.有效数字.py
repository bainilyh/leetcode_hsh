# #
# # @lc app=leetcode.cn id=65 lang=python3
# #
# # [65] 有效数字
# #
# # 解题思路:
# # 1. 使用有限状态自动机(DFA)来解决这个问题
# # 2. 定义状态转移字典,包含所有可能的状态转移
# # 3. 遍历字符串,根据当前字符和状态进行状态转移
# # 4. 最后判断是否在合法的终止状态
# #
# # 数据结构:
# # - 字典: 存储状态转移规则
# # - 集合: 存储合法的终止状态
# #
# # 时间复杂度: O(n), n为字符串长度
# # 空间复杂度: O(1), 状态转移表是固定大小

# # @lc code=start
# class Solution:
#     def isNumber(self, s: str) -> bool:
#         # 定义状态转移字典
#         states = {
#             0: {'digit': 1, 'sign': 2, 'dot': 3},
#             1: {'digit': 1, 'dot': 4, 'e': 5},
#             2: {'digit': 1, 'dot': 3},
#             3: {'digit': 4},
#             4: {'digit': 4, 'e': 5},
#             5: {'digit': 7, 'sign': 6},
#             6: {'digit': 7},
#             7: {'digit': 7}
#         }
        
#         # 定义终止状态
#         final_states = {1, 4, 7}
        
#         # 当前状态初始化为0
#         curr_state = 0
        
#         # 遍历字符串
#         for c in s.lower():
#             if c.isdigit():
#                 c = 'digit'
#             elif c in ['+', '-']:
#                 c = 'sign'
#             elif c in ['e', 'E']:
#                 c = 'e'
#             elif c == '.':
#                 c = 'dot'
#             else:
#                 return False
                
#             # 如果当前输入在状态转移表中不存在,返回False
#             if c not in states[curr_state]:
#                 return False
                
#             # 状态转移
#             curr_state = states[curr_state][c]
            
#         # 判断是否在合法的终止状态
#         return curr_state in final_states

# # @lc code=end
