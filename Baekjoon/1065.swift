//한수

var input: Int = Int(readLine()!)!

if input < 100 {
    print(input)
} else {
    if input == 1000 {
        input -= 1
    }
    var count: Int = 99
    var num: Int = 100
    while num <= input {
        let first: Int = num / 100
        let second: Int = (num - first * 100) / 10
        let third: Int = num - first * 100 - second * 10
        if second * 2 == first + third {
            count += 1
        }
        num += 1
    }
    print(count)
}
