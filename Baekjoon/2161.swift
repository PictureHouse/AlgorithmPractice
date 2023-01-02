//카드1 

let input: Int = Int(readLine()!)!

var list: [Int] = []
var index: Int = 1
while index <= input {
    list.append(index)
    index += 1
}

while !list.isEmpty {
    print(list.removeFirst(), terminator: " ")
    if !list.isEmpty {
        list.append(list.removeFirst())
    }
}

