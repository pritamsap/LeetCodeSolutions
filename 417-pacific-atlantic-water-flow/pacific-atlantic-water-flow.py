class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols  = len(heights), len(heights[0])
        pac, atl = set(), set()


        # for the first value, we pass it's same value as prevHeight
        # the top border guaratees touches the pacific
        # the bottom border guaratees touches the atlantic
        def dfs(r, c, visit, prevHeight):
            if(r, c) in visit or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight:
                return
            
            visit.add((r, c))

            # explore all four direction
            # now we here we prevHeight Make sense
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])



       # top border touches pacific, bottom border touches atlantic
        for c in range(cols):
            # pacific top row
            dfs(0, c, pac, heights[0][c])
            # atlantic bottom row
            dfs(rows-1, c, atl, heights[rows-1][c])

        # left column touches pacific, right column touches atlantic
        for r in range(rows):
            # pacific left col
            dfs(r, 0, pac, heights[r][0])
            #atlantic right col
            dfs(r, cols-1, atl, heights[r][cols-1])

        # append to res that touches are in both atl and pacfic sets
        res = []
        for r  in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])


        return res

        