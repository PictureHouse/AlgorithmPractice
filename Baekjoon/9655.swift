//돌 게임

var n = Int(readLine()!)!

var turn = true
while n != 0 {
    if n - 3 >= 0 {
      n -= 3
      turn.toggle()
    } else {
      n -= 1
      turn.toggle()
    }
}

turn.toggle()
print(turn ? "SK" : "CY")
