//드론 조작

let input = readLine()!.split(separator: " ")
let n = Int(input[0])!
let k = Int(input[1])!

var blocks = [(Int, Int)]()
for _ in 0..<n {
    let tmp = readLine()!.split(separator: " ")
    blocks.append((Int(tmp[0])!, Int(tmp[1])!))
}

var moves = readLine()!

var drone = (0, 0)
while !moves.isEmpty {
    let move = moves.removeFirst()
    switch move {
    case "U":
        let next = (drone.0, drone.1 + 1)
        if !blocks.contains(where: { $0 == next } ) {
            drone = next
        }
    case "D":
        let next = (drone.0, drone.1 - 1)
        if !blocks.contains(where: { $0 == next } ) {
            drone = next
        }
    case "R":
        let next = (drone.0 + 1, drone.1)
        if !blocks.contains(where: { $0 == next } ) {
            drone = next
        }
    case "L":
        let next = (drone.0 - 1, drone.1)
        if !blocks.contains(where: { $0 == next } ) {
            drone = next
        }
    default:
        continue
    }
}

print("\(drone.0) \(drone.1)")

