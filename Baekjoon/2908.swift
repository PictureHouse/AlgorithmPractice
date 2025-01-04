//상수

var input = readLine()!.split(separator: " ")

var nums: [Int] = []
for i in input {
    nums.append(Int(String(i.reversed()))!)
}

print(nums.max()!)

