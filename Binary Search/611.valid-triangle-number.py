#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#

# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)

        for k in range(n-1, 1, -1):   # pick largest side
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # all pairs (i..j-1, j, k) are valid
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        return count
        
# @lc code=end

