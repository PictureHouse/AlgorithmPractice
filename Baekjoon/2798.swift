//블랙잭

let input1: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}
let n: Int = input1[0]
let m: Int = input1[1]
let input2: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}

var sum: Int = 0
var dif: Int = m - sum
var result: Int = 0

var index1: Int = 0
while index1 < n - 2 {
    var index2: Int = index1 + 1
    while index2 < n - 1 {
        var index3: Int = index2 + 1
        while index3 < n {
            sum = input2[index1] + input2[index2] + input2[index3]
            dif = m - sum
            if dif >= 0 && dif < (m - result) {
                result = sum
            }
            index3 += 1
        }
        index2 += 1
    }
    index1 += 1
}
print(result)

