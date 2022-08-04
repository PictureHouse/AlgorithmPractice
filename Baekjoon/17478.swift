//재귀함수가 뭔가요?

let input: [Int] = readLine()!.split(separator: " ").map{Int(String($0))!}
let n: Int = input[0]
let count : Int = 0

func recursion(n: Int, count: Int) -> Void {
    let underBar: String = String(repeating: "____", count: count)
    if n == 0 {
        print(underBar+"\"재귀함수가 뭔가요?\"")
        print(underBar+"\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print(underBar+"라고 답변하였지.")
        return
    }
    print(underBar+"\"재귀함수가 뭔가요?\"")
    print(underBar+"\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
    print(underBar+"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print(underBar+"그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
    recursion(n: n - 1, count: count + 1)
    print(underBar+"라고 답변하였지.")
}

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
recursion(n: n, count: count)
