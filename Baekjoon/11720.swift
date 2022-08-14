//숫자의 합

let num: Int = Int(readLine()!)!
var nums: String = readLine()!

var sum: Int = 0
var index: Int = 0
while index < num {
    sum += Int(String(nums.removeFirst()))!
    index += 1
}
print(sum)
