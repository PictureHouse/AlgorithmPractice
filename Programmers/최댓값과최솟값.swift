func solution(_ s:String) -> String {
    var nums = s.split(separator: " ").map { Int($0)! }
    nums.sort()
    let min = nums[0]
    let max = nums.last!
    return "\(min) \(max)"
}
