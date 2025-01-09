//줄 세우기

let num = Int(readLine()!)!
var input = [String]()
for _ in 0..<num {
    input.append(readLine()!)
}

if input == input.sorted() {
    print("INCREASING")
} else if input == input.sorted().reversed() {
    print("DECREASING")
} else {
    print("NEITHER")
}
