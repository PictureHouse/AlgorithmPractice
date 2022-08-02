//두 수 비교하기

let input: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))!}
let a: Int = input[0]
let b: Int = input[1]

if a>b {
    print(">")
} else if a<b {
    print("<")
} else {
    print("==")
}
