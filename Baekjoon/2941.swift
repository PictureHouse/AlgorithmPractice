//크로아티아 알파벳

let input: String = readLine()!

var count: Int = 0
var flag: Character = "?"
for char in input {
    switch char {
    case "c":
        flag = "c"
    case "d":
        flag = "d"
    case "l":
        flag = "l"
    case "n":
        flag = "n"
    case "s":
        flag = "s"
    case "z":
        if flag == "d" {
            flag = "!"
        } else {
            flag = "z"
        }
    case "=":
        if flag == "c" || flag == "s" || flag == "z" {
            count += 1
            flag = "?"
        } else if flag == "!" {
            count += 2
            flag = "?"
        }
    case "-":
        if flag == "c" || flag == "d" {
            count += 1
            flag = "?"
        }
    case "j":
        if flag == "l" || flag == "n" {
            count += 1
            flag = "?"
        }
    default:
        flag = "?"
        break
    }
    
}
print(input.count - count)
