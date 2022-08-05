//소트인사이드

var num: [Int] = Array(readLine()!).map{Int(String($0))!}

num.sort(by: >)
for i in num {
    print(i, terminator: "")
}
