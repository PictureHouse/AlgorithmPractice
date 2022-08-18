//2007년

let date: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}

var month: Int = 1
var day: Int = 1
var count: Int = 0

while month < date[0] {
    switch month {
    case 1,3,5,7,8,10,12:
        count += 31
    case 4,6,9,11:
        count += 30
    case 2:
        count += 28
    default:
        count += 0
    }
    month += 1
}

while day < date[1] {
    count += 1
    day += 1
}

switch count % 7 {
case 0:
    print("MON")
case 1:
    print("TUE")
case 2:
    print("WED")
case 3:
    print("THU")
case 4:
    print("FRI")
case 5:
    print("SAT")
case 6:
    print("SUN")
default:
    print("Error")
}
