#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        visited = [[False] * m for _ in range(n)]
        def dfs(board, i, j, visited, word, cur_word_index):
            if cur_word_index >= len(word):
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            if board[i][j] != word[cur_word_index]:
                return False
            if visited[i][j]:
                return False
            visited[i][j] = True
            ret = dfs(board, i - 1, j, visited, word, cur_word_index + 1) or \
                    dfs(board, i + 1, j, visited, word, cur_word_index + 1) or \
                    dfs(board, i, j - 1, visited, word, cur_word_index + 1) or \
                    dfs(board, i, j + 1, visited, word, cur_word_index + 1)
            if ret:
                return True
            else:
                visited[i][j] = False
                return False
            
        for i in range(n):
            for j in range(m):
                if dfs(board, i, j, visited, word, 0):
                    return True
        return False
            
# @lc code=end

