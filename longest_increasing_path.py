### Longest increasing path.
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        mem = [[0]*col for i in range(row)]
       
        def dfs(u,v):
            if mem[u][v] == 0:
                res = 1
                for i, j in [(0,1), (1,0), (-1,0), (0,-1)]:
                    dx, dy = u+i, v+j
                    if 0 <= dx < row and 0 <= dy < col and matrix[dx][dy] > matrix[u][v]:
                        res = max(dfs(dx,dy)+1, res)
                mem[u][v] = res
            return mem[u][v]
        result = 0
        for i in range(row):
            for j in range(col):
                result = max(result, dfs(i,j))

        return result 
