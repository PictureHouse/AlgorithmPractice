//막대기

var x = Int(readLine()!)!

let piece = [64, 32, 16, 8, 4, 2, 1]
var count = 0
for i in piece {
    if x - i >= 0 {
      x -= i
      count += 1
    }
}
print(count)
