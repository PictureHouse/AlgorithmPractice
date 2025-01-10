//쉽게 푸는 문제

let input = readLine()!.split(separator: " ")
let a = Int(input[0])!
let b = Int(input[1])!

var num = 1
var count = 0
var sum = 0
for i in 1...b {
    if count < num {
        if i >= a {
            sum += num
        }
    } else {
        num += 1
        count = 0
        if i >= a {
            sum += num
        }
    }
    count += 1
}

print(sum)
