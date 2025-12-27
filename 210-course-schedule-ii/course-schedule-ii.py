class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        visited = set()
        memo = set()
        res = []

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        def dfs(crs):
            if crs in visited:
                return False
            
            # if res size is greater than crs, we know course is already there or not
            if crs in memo:
                return True        
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            visited.remove(crs)
            memo.add(crs)
            res.append(crs)
            preMap[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c): return []
        return res

            


        