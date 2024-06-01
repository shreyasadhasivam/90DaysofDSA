class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = float('-inf')
        currentSum = 0
        
        for num in nums:
            currentSum += num
            
            if currentSum > maxSum:
                maxSum = currentSum
            
            if currentSum < 0:
                currentSum = 0
        
        return maxSum