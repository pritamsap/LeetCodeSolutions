class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        def dfs(r, c, area):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "#" or grid [r][c] == 0:
                return 0
            
            # grid position is 1
            grid[r][c] = "#"
            area += 1
            area += dfs(r + 1, c, 0)
            area +=dfs(r - 1, c, 0)
            area += dfs(r, c + 1, 0)
            area += dfs(r, c - 1, 0)
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = dfs(r, c, 0)
                    maxArea = max(maxArea, res)    
        
        return maxArea 




        