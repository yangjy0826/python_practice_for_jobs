# My code beats 70% of the submissions:
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        n_out = 0
        for i in range(int(len(nums)/2)):
            n_out += nums[2*i]
        return n_out

# Other's solution that can avvoid loop:
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        return sum(nums[::2]) # 每隔一个取一个元素（原list的0,2,4,6,8……项）