//세 수

var input: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}

input.sort()
print(input[1])
