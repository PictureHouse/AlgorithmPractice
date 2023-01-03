//이장님 초대

var num: Int = Int(readLine()!)!
var trees: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}

var days: [Int] = [Int](repeating: 0, count: trees.count)
var index: Int = 1
while index <= days.count {
    days[index - 1] = index
    index += 1
}
trees.sort(by: >)
index = 0
while index < days.count {
    days[index] += trees[index]
    index += 1
}
print(days.max()! + 1)

