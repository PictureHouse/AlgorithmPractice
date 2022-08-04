//나머지

let input: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}
let a: Int = input[0]
let b: Int = input[1]
let c: Int = input[2]

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
