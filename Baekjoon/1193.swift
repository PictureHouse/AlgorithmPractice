//분수찾기

let input: Int = Int(readLine()!)!

var numerator: Int = 1
var denominator: Int = 1
var count: Int = 1
var rightFlag: Int = 1
var leftFlag: Int = 0

while count != input {
    if rightFlag == 1 && numerator == 1 {
        denominator += 1
        rightFlag = 0
        leftFlag = 1
    } else if rightFlag == 1 {
        numerator -= 1
        denominator += 1
    } else if leftFlag == 1 && denominator == 1 {
        numerator += 1
        leftFlag = 0
        rightFlag = 1
    } else if leftFlag == 1 {
        numerator += 1
        denominator -= 1
    }
    count += 1
}
print("\(numerator)/\(denominator)")
