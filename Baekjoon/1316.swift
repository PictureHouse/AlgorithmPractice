//그룹 단어 체커

let input: Int = Int(readLine()!)!

var count: Int = 0
var flag: Int = 1
var index: Int = 0
while index < input {
    flag = 1
    var word: String = readLine()!
    if word.count == 1 {
        count += 1
    } else {
        var check: Character = word.removeFirst()
        while word.count != 0 {
            let tmp: Character = word.removeFirst()
            if check != tmp && !word.contains(check) {
                check = tmp
            } else if check != tmp && word.contains(check) {
                flag -= 1
                break
            }
        }
        if flag == 1 {
            count += 1
        }
    }
    index += 1
}
print(count)
