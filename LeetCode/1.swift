//Two Sum

class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var result: [Int] = []
        loop1: for i in 0...nums.count-2 {
            loop2: for j in 1...nums.count-1 {
                if i != j && nums[i] + nums[j] == target {
                    result.append(i)
                    result.append(j)
                    break loop1
                }
            }
        }
        return result
    }
}
