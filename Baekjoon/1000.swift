//A+B

let input: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))!}
var result: Int = 0

for num in input {
    result += num
}
print(result)
