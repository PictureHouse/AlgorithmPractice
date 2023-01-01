//제로

let input_num: Int = Int(readLine()!)!

var nums: [Int] = []
var index: Int = 0
while index < input_num {
    let input: Int = Int(readLine()!)!
    if input == 0 {
        nums.removeLast()
    } else {
        nums.append(input)
    }
    index += 1
}

index = 0
var sum: Int = 0
while index < nums.count {
    sum += nums[index]
    index += 1
}
print(sum)
