//개수 세기

let numOfInput = Int(readLine()!)!
let input = readLine()!.split(separator: " ").map { Int($0)! }
let num = Int(readLine()!)!

var count = 0
for i in input {
    if i == num {
        count += 1
    }
}
print(count)
