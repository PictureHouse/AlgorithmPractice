//꼬마 정민

let input = readLine()!.split(separator: " ").map { Int($0)! }

let result = input.reduce(0, +)
print(result)
