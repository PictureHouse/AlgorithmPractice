//팩토리얼

let input: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}
let n: Int = input[0]

func factorial(n: Int) -> Int {
    if n == 0 {
        return 1
    }
    return n * factorial(n: n - 1)
}

print(factorial(n: n))
