//명령 프롬프트 

let input_num: Int = Int(readLine()!)!

var arr: [Character] = Array(readLine()!)
if input_num != 1 {
    var index: Int = 0
    while index < input_num - 1 {
        let tmp: [Character] = Array(readLine()!)
        var i: Int = 0
        while i < arr.count {
            if arr[i] != tmp[i] {
                arr[i] = "?"
            }
            i += 1
        }
        index += 1
    }
}
let result: String = String(arr)
print(result)

