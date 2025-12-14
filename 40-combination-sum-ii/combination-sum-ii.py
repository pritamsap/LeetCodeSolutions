class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # pretty subset problem for for combination
        # each number maybe used once in the combination
        # use the number or not useit 


        res = []
        candidates.sort()
        def dfs(i, curr, total):  
            if total == target:
                res.append(curr[:])
                return

            if total > target or i >= len(candidates):
                return

            # decision include
            curr.append(candidates[i])
            dfs(i+1, curr, total + candidates[i])
            curr.pop()

            # decision not include
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i +=1
            dfs(i+1, curr, total)

        dfs(0, [], 0)
        return res

        