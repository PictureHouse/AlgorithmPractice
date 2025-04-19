// 1.Two Sum

class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        let count = nums.count
        var result: [Int] = []

        for i in 0..<count {
            for j in i+1..<count {
                if nums[i] + nums[j] == target {
                    result = [i, j]
                    break
                }
            }
        }
        return result
    }
}
