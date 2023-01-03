//뒤집기 

var input: String = readLine()!

var block: Int = 0
var tmp1: Character = input.removeFirst()
while !input.isEmpty {
    let tmp2: Character = input.removeFirst()
    if tmp1 != tmp2 {
        block += 1
        tmp1 = tmp2
    }
}
block += 1
print(block / 2)

