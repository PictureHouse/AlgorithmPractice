//모음의 개수

var word: String = readLine()!

var index: Int = 0
var count: Int = 0
while index < word.count {
    let char: Character = word.removeFirst()
    switch char{
    case "a", "e", "i", "o", "u":
        count += 1
    default:
        count += 0
    }
}
print(count)
