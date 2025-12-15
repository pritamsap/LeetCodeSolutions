class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # array of daily temp
        # return answer array answer[i] is the num of day you wait for ith day
        # ith day to get warm
        # [30, 40, 50, 60]
        # [1, 1, 1, 0]
        # for the last index it will be 0
        # stack: [30]
        # if stack and temp[i] > stack[-1]
        # set the warm day
        # [71] 69 < 71 -> [71, 69]
        # while stack 71 - 69 pop, i[71] - i[69] append
        # 72 > 71, pop 71 ,append index differnet from 72 to 71


        # stores (temp, index)
        stack = []
        warmArray = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(stack) >= 1 and temperatures[i] > stack[-1][0]:
                temp, index = stack.pop()
                warmArray[index] = i - index
            
            stack.append((temperatures[i], i))
        
        return warmArray



        # [76, 73]



        