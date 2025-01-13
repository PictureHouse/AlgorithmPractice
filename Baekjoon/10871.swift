//X보다 작은 수

let nums = readLine()!.split(separator: " ").map { Int($0)! }
let input = readLine()!.split(separator: " ").map { Int($0)! }

for i in input {
    if i < nums[1] {
        print(i, terminator: " ")
    }
}
