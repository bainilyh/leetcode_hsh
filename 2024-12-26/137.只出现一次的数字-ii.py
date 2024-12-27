# # @lc code=start
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         # 使用一个int32来记录每个bit的出现次数
#         count = 0
#         for i in range(32):
#             # 遍历每个数字
#             for num in nums:
#                 # 通过移位和mask来判断当前bit是否为1
#                 if (num >> i) & 1:
#                     count += 1
#             # 如果当前bit出现次数为3的倍数，res的该bit为0
#             if count % 3 == 0:
#                 res &= ~(1 << i)
#             # 否则，res的该bit为1
#             else:
#                 res |= 1 << i
#         return res

# # @lc code=end

# # 解题思路:
# # 1. 使用一个int32来记录每个bit的出现次数
# # 2. 遍历每个数字
# # 3. 通过移位和mask来判断当前bit是否为1
# # 4. 如果当前bit出现次数为3的倍数，res的该bit为0
# # 5. 否则，res的该bit为1
# # 6. 最后将res返回

# # 数据结构:
# # - 一个int32来记录每个bit的出现次数
# # - 一个int32来存储结果

# # 算法:
# # - 遍历每个数字
# # - 通过移位和mask来判断当前bit是否为1
# # - 通过count来判断当前bit出现次数是否为3的倍数

# # 时间复杂度: O(n) - 只需要遍历一次数组
# # 空间复杂度: O(1) - 只使用了常数个变量
