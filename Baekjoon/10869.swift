let input: [Int] = readLine()!.split(separator: " ").map{ Int(String($0))! }

func add(a: Int, b: Int) -> Int { return a + b }

func sub(a: Int, b: Int) -> Int { return a - b }

func mul(a: Int, b: Int) -> Int { return a * b }

func div(a: Int, b: Int) -> Int { return a / b }

func rem(a: Int, b: Int) -> Int { return a % b }

print(add(a: input[0], b: input[1]))
print(sub(a: input[0], b: input[1]))
print(mul(a: input[0], b: input[1]))
print(div(a: input[0], b: input[1]))
print(rem(a: input[0], b: input[1]))
