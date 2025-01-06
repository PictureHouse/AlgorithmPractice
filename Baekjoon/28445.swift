//알록달록 앵무새

let father = readLine()!.split(separator: " ")
let mother = readLine()!.split(separator: " ")

let fatherSet = Set(father)
let motherSet = Set(mother)
let colorSet = fatherSet.union(motherSet)
var color = Array(colorSet)
color.sort()

for i in color {
    for j in color {
    	print("\(i) \(j)")
    }
}
