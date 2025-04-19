// 56.Merge Intervals

class Solution {
    func merge(_ intervals: [[Int]]) -> [[Int]] {
        var n = intervals.count
        var arr = intervals
        var result: [[Int]] = []

        arr.sort { $0[0] < $1[0] }
        var tmp = [0, 0]
        for i in 0..<n {
            if i == 0 {
                tmp = arr[i]
            } else {
                if tmp[1] >= arr[i][0] {
                    tmp = [min(tmp[0], arr[i][0]), max(tmp[1], arr[i][1])]
                } else {
                    result.append(tmp)
                    tmp = arr[i]
                }
            }
        }
        result.append(tmp)

        return result
    }
}
