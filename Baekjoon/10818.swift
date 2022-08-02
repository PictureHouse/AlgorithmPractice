let input: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))!}
let nums: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))!}

var min: Int = nums[0]
var max: Int = nums[0]

for num in nums {
    if num < min {
        min = num
    } else if num > max {
        max = num
    }
}

print(min, max)
