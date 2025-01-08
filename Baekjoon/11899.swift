//괄호 끼워넣기

var input = readLine()!
var brackets = [Character]()
while !input.isEmpty {
    brackets.append(input.removeFirst())
}

var stack = [Character]()
for b in brackets {
    switch b {
    case "(":
        stack.append(b)
    case ")":
        if stack.last == "(" {
            stack.removeLast()
        } else {
            stack.append(b)
        }
    default:
        print("error")
    }
}

print(stack.count)

