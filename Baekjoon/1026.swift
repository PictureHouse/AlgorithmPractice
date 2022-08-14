//보물

let num: Int = Int(readLine()!)!
var A: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}
var B: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}

var result: Int = 0
while !A.isEmpty && !B.isEmpty {
    let a: Int = A.min()!
    A.remove(at: A.firstIndex(of: a)!)
    let b: Int = B.max()!
    B.remove(at: B.firstIndex(of: b)!)
    result += a * b
}
print(result)
