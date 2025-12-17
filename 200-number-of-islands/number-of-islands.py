class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        totalIslands = 0

        def dfs(r, c):

            # if r, c invalid or it's # or 0
            # go back
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "#" or grid[r][c] == "0":
                return  

            # r, c is a 1
            # set as marked
            grid[r][c] = "#"

            # traverse all four directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    totalIslands += 1
        return totalIslands
        
    


        