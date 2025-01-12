//문자열

let num = Int(readLine()!)!
var inputs = [String]()
for _ in 0..<num {
    inputs.append(readLine()!)
}

for input in inputs {
    print("\(input.first!)\(input.last!)")
}
