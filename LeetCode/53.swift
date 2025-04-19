// 53.Maximum Subarray

class Solution {
    func maxSubArray(_ nums: [Int]) -> Int {
        var currentSum = 0
        var maxSum = nums[0]

        for num in nums {
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)
        }

        return maxSum
    }
}
