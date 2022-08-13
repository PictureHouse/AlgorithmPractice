//접미사 배열

let input: String = String(readLine()!)

var list: [String] = []
var length: Int = 0
while length <= input.count {
    list.append(String(input.suffix(length)))
    length += 1
}
list.remove(at: 0)
list.sort()
for sortedSuffix in list {
    print(sortedSuffix)
}
