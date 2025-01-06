//I've Been Everywhere, Man

let numOfCases = Int(readLine()!)!
var result = [Int]()

for _ in 0..<numOfCases {
    let numOfTrips = Int(readLine()!)!
    var cities = Set<String>()
  
    for _ in 0..<numOfTrips {
    	let city = readLine()!
    	cities.insert(city)
    }
    result.append(cities.count)
}

for i in result {
    print(i)
}
