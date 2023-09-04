let abc = 0
const def = 69

console.log(abc)

abc = abc + 1

console.log(abc)

console.log(def)

abc = 0
console.log("Activating Loop")
while (abc <= 50) {
    if (abc > 25) {
        console.log(abc)
    } else {
        console.log("Number hidden until 25")
    }
    abc += 1
}