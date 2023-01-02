//성적 통계 

let input: Int = Int(readLine()!)!

var result: [String] = []
var index: Int = 0
while index < input {
    var list: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))! }
    let num: Int = list.removeFirst()
    list.sort()
    var gap: [Int] = []
    var i: Int = 0
    while i < num - 1 {
        gap.append(list[i + 1] - list[i])
        i += 1
    }
    result.append("Max \(list[num - 1]), Min \(list[0]), Largest gap \(gap.max()!)")
    index += 1
}

index = 0
while index < result.count {
    print("Class \(index + 1)")
    print(result[index])
    index += 1
}

