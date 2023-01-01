//방 번호

var num: String = readLine()!

var nums: [Int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
var index: Int = 0
let size: Int = num.count
while index < size {
    let tmp: Int = Int(String(num.removeFirst()))!
    nums[tmp] += 1
    index += 1
}
if nums[6] != 0 || nums[9] != 0 {
    nums[6] = (nums[6] + nums[9] + 1) / 2
    nums[9] = 0
}
print(nums.max()!)

