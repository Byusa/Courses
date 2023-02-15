// Array interation: 8 mothods

// 1) forEach
let numbArray = [9,12,11]
numbArray.forEach((item, index) =>{
    console.log(item, index);
})

//2) map 
const doubled = numbArray.map((item)=> {
    return item  * 2;
})
console.log(doubled)

//3) filter  (remove 12)
const removeTwelve = numbArray.filter((item) => {
    return item!==12
})
console.log(removeTwelve)


//4) reduce (do something with all the numbers)
const sum = numbArray.reduce((result, item) => {
    return result + item
}, 0)
console.log(sum)

//5) some ( is any meet condition) [true, false]
let isbiggerThanTen = numbArray.some((item) =>{
    return item>10
})
console.log(isbiggerThanTen)

//6) Every ( is every meet condition)[true, false]
isbiggerThanTen = numbArray.every((item) =>{
    return item>10
})
console.log(isbiggerThanTen)

//7) find 
const numbObjects = [{id: 9}, {id: 4}, {id: 8}]
const found = numbObjects.find((item) => {
    return item.id === 4
})
console.log(found) // if not found returns undefined

//8) find index (find the index)
const foundIndex = numbObjects.findIndex((item) => {
    return item.id === 4
})
console.log(foundIndex)

















