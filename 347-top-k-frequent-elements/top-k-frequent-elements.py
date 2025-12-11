class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # returns the most frequent numbers 
        # [1,1,1,2,2,3], k = 2
        # [1, 2]
        # 2 most frequent elemenst are 1 and 2

        # First thought: hashMap with counter
        # at the end return the top k frequent elements

        hashMap = {}

        # empty list
        freq = [[] for i in range(len(nums) + 1)]


        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1


        for key, val in hashMap.items():
            freq[val].append(key)


        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        