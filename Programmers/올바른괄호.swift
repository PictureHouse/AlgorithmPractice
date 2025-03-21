import Foundation

func solution(_ s:String) -> Bool
{
    var stack: [Character] = []
    
    for i in s {
        if stack.isEmpty {
            stack.append(i)
        } else {
            if i == "(" {
                stack.append(i)
            } else {
                if stack.last! == "(" {
                    stack.removeLast()
                } else {
                    stack.append(i)
                }
            }
        }
    }
    
    if stack.isEmpty {
        return true
    } else {
        return false
    }
}
