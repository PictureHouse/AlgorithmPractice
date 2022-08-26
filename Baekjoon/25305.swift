//커트라인

let input: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}
var list: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}
list.sort()
print(list[list.count - input[1]])
