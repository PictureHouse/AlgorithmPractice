// 20.Valid Parentheses

class Solution {
    func isValid(_ s: String) -> Bool {
        var stack: [Character] = []

        for b in s {
            if b == "(" || b == "{" || b == "[" {
                stack.append(b)
            } else {
                if b == ")" {
                    if stack.last == "(" {
                        stack.removeLast()
                    } else {
                        stack.append(b)
                    }
                } else if b == "}" {
                    if stack.last == "{" {
                        stack.removeLast()
                    } else {
                        stack.append(b)
                    }
                } else {
                    if stack.last == "[" {
                        stack.removeLast()
                    } else {
                        stack.append(b)
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
}
