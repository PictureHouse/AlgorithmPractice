//합

let input: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}
let n: Int = input[0]

var result: Int = 0
for num in 1...n {
    result += num
}
print(result)
