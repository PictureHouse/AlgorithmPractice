//N번째 큰 수

let numOfInputs = Int(readLine()!)!

var results = [Int]()
for _ in 0..<numOfInputs {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    results.append(input.sorted()[7])
}

for i in results {
    print(i)
}
