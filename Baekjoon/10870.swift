//피보나치 수 5

let input: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}
let n: Int = input[0]

func fibonacci(n: Int) -> Int {
    if n == 0 {
        return 0
    } else if n == 1 {
        return 1
    }
    return fibonacci(n: n - 1) + fibonacci(n: n - 2)
}

print(fibonacci(n: n))
