class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # find all regions that are reachable from edge cases
        rows = len(board)
        cols = len(board[0])

        reachSet = set()

        def dfs(r, c, reachSet):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] == "X" or (r, c) in reachSet:
                return
            
            reachSet.add((r, c))
            #traverse all four directions
            dfs(r+1, c, reachSet)
            dfs(r-1, c, reachSet)
            dfs(r, c+1, reachSet)
            dfs(r, c-1, reachSet)


        # start with top and bottom row 
        for c in range(cols):
            dfs(0, c, reachSet)
            dfs(rows-1, c, reachSet)

        # left and right cols
        for r in range(rows):
            dfs(r, 0, reachSet)
            dfs(r, cols-1, reachSet)
        
        # loop through all element to see if it's not in reachSet
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in reachSet:
                    board[r][c] = "X"
        


                

        