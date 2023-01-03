//백대열    

var nums: [Int] = readLine()!.split(separator: ":").map{Int(String($0))!}

var flag: Int = 0
while flag != 1 {
    var tmp: Int = nums.min()!
    while tmp != 1 {
        if nums[0] % tmp == 0 && nums[1] % tmp == 0 {
            nums[0] = nums[0] / tmp
            nums[1] = nums[1] / tmp
            break
        }
        tmp -= 1
    }
    if tmp == 1 {
        flag = 1
    }
}
print("\(nums[0]):\(nums[1])")

