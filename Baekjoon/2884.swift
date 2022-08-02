let input: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))!}

var h: Int = input[0]
var m: Int = input[1]

if m < 45 {
    if h - 1 >= 0 {
        h -= 1
    } else {
        h = 24 - 1
    }
    m = 60 - (45 - m)
} else {
    m -= 45
}

print(h, m)
