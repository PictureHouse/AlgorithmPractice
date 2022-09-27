import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var result: [Int] = []
    
    var index: Int = 0
    while index < commands.count {
        let i: Int = commands[index][0]
        let j: Int = commands[index][1]
        let k: Int = commands[index][2]
        
        var head_cut = array.dropFirst(i - 1)
        var tail_cut = head_cut.dropLast(array.count - j)
        tail_cut.sort()

        result.append(tail_cut[tail_cut.startIndex + k - 1])
        index += 1
    }
    
    return result
}

