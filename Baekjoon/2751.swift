//수 정렬하기 2

let numOfInput: Int = Int(readLine()!)!

var count: Int = 0
var nums: [Int] = []
while count < numOfInput {
    nums.append(Int(readLine()!)!)
    count += 1
}

nums.sort()
for num in nums {
    print(num)
}
