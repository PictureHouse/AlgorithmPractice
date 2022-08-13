//일곱 난쟁이

var input: [Int] = []
var index: Int = 0
while index < 9 {
    input.append(Int(readLine()!)!)
    index += 1
}

var sum: Int = 0
for height in input {
    sum += height
}
a:for i in 0...input.count - 2 {
b:  for j in 1...input.count - 1 {
        if i != j && input[i] + input[j] == sum - 100 {
            input.remove(at: j)
            input.remove(at: i)
            break a
        }
    }
}
input.sort()

for height in input {
    print(height)
}
