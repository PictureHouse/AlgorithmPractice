//곱셈

var first: [Character] = readLine()!.map{Character(String($0))}
var second: [Character] = readLine()!.map{Character(String($0))}

var num0: Int = first[0].wholeNumberValue! * 100 + first[1].wholeNumberValue! * 10 + first[2].wholeNumberValue!
var num1: Int = second[2].wholeNumberValue!
var num2: Int = second[1].wholeNumberValue!
var num3: Int = second[0].wholeNumberValue!

let result1: Int = num0 * num1
let result2: Int = num0 * num2
let result3: Int = num0 * num3
let result4: Int = result1 + result2 * 10 + result3 * 100

print(result1)
print(result2)
print(result3)
print(result4)
