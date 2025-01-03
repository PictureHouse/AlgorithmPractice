//파일 정리

let num = Int(readLine()!)!
var formats: [String] = []
for _ in 1...num {
    let input = readLine()!
    let format = input.split(separator: ".")
    formats.append(String(format[1]))
}

formats.sort()

var result: [(String, Int)] = []
var tmp = (formats[0], 0)
for f in formats {
    if f != tmp.0 {
        result.append(tmp)
        tmp = (f, 1)
    } else {
        tmp.1 += 1
    }
}
result.append(tmp)

for r in result {
    print("\(r.0) \(r.1)")
}
