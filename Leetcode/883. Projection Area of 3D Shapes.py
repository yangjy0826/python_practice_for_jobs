class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum_up = 0
        sum_front = 0
        sum_back = 0
        grid_all = []
        for i in range(len(grid)):
            sum_front+=max(grid[i])
            grid_all += grid[i]
            for j in range(len(grid[i])):
                if grid[i][j]!=0:
                    sum_up += 1
        for i in range(len(grid)):
            sum_back+=max(grid_all[i::len(grid[i])])
        return sum_up+sum_front+sum_back