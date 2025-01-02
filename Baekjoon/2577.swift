//숫자의 개수

var nums: [Int] = []
for _ in 0...2 {
    let input = Int(readLine()!)!
    nums.append(input)
}

let multiplied = String(nums[0] * nums[1] * nums[2])

var result: [Int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in multiplied {
    let index = Int(String(i))!
    result[index] += 1
}

for j in result {
    print(j)
}
