//동일한 단어 그룹화하기

let num = Int(readLine()!)!
var words = [[Character]]()

for _ in 0..<num {
    var input = readLine()!
    var characters = [Character]()
    while !input.isEmpty {
    	characters.append(input.removeFirst())
    }
    characters.sort()
    if !words.contains(characters) {
    	words.append(characters)
    }
}

print(words.count)
