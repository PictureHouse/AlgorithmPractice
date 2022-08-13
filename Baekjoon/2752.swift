//세수정렬

var input: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}

input.sort()
for num in input {
    print(num, terminator: " ")
}
