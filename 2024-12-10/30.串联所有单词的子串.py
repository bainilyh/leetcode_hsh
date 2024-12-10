#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # if not s or not words:
        #     return []
        
        # word_len = len(words[0])  # 每个单词的长度
        # total_len = word_len * len(words)  # 所有单词连接后的总长度
        # word_count = Counter(words)  # 统计每个单词出现的次数
        # result = []

        # # 遍历所有可能的起始位置
        # for i in range(len(s) - total_len + 1):
        #     seen = Counter()  # 用于统计当前窗口中的单词
        #     valid = True

        #     # 检查从i开始的子串
        #     for j in range(i, i + total_len, word_len):
        #         word = s[j: j + word_len]
        #         if word in word_count:
        #             seen[word] += 1
        #             if seen[word] > word_count[word]:
        #                 valid = False
        #                 break
        #         else:
        #             valid = False
        #             break

        #     if valid:
        #         result.append(i)

        # return result

# @lc code=end

# 解题思路：
# 1. 使用滑动窗口的方法，遍历所有可能的起始位置。
# 2. 对于每个起始位置，检查从该位置开始的子串是否符合要求。
# 3. 使用Counter来统计单词出现的次数，以便快速判断。

# 数据结构：
# - 字符串（s）：用于存储原始字符串。
# - 列表（words）：存储需要匹配的单词。
# - Counter：用于统计单词出现的次数。

# 算法：
# - 滑动窗口：遍历所有可能的起始位置。
# - 哈希表（Counter）：用于快速统计和比较单词出现的次数。

# 时间复杂度：O(n * m * k)
# 其中n是字符串s的长度，m是words中单词的数量，k是每个单词的长度。
# 我们需要遍历字符串s的每个可能起始位置，对于每个位置，我们需要检查m个单词。

# 空间复杂度：O(m)
# 我们使用了两个Counter对象，它们的大小与words中不同单词的数量相关，最坏情况下为O(m)。
