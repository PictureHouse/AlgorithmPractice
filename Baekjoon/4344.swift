import Foundation
let caseNum: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}
let count: Int = caseNum[0]

var i: Int = 0
while i < count {
    let nums: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}
    var sum: Int = 0
    var index: Int = 1
    while index <= nums[0] {
        sum += nums[index]
        index += 1
    }
    let mean: Double = Double(sum) / Double(nums[0])
    index = 1
    var biggerThanMean: Int = 0
    while index <= nums[0] {
        if Double(nums[index]) > mean {
            biggerThanMean += 1
        }
        index += 1
    }
    let percent: Double = Double(biggerThanMean) / Double(nums[0]) * 100
    print(String.init(format: "%.3f", percent)+"%")
    i += 1
}
