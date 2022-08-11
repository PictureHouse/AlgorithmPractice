//ATM

let input: Int = Int(readLine()!)!
var nums: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}
nums.sort()

var time: Int = 0
var list: [Int] = []
var min: Int = 0
var index: Int = 0
while index < nums.count {
    time += nums[index]
    list.append(time)
    index += 1
}
var sum: Int = 0
for num in list {
    sum += num
}
print(sum)
