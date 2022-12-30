// Reference Vs Primitive Values
// Primitive values (strings, numbers, boolean, undefined, Null, Symbol(ES6))
// store on stack which is fast
let name = "serge"
console.log(name)
let secondName = name
console.log(secondName)
name = "Byusa"
console.log(name)
console.log(secondName)

// Reference Values (Object, Arrays)
// store on heap and not fast and does not able to hold a lot of memory
let person = {
    age: 29,
    name: "Byusa",
    hobies: ["Basketball",'Cooking']
}
console.log(person)
let secondPerson = person
console.log(secondPerson)
secondPerson.name = "Beza" // we only copied the pointer not the value
console.log(person) // we changed secondPerson but person got changed too

// to fix it, create a new object
let thirdPerson = {
    age: 29,
    name: "Byusa",
    hobies: ["Basketball",'Cooking']
}
console.log(thirdPerson)




// Coping an object
let copyPerson = Object.assign({}, person) //shalow clone (so array will still be reference)
console.log(copyPerson)

// Deep clone (you can use a library)

// Coping an array
let arr = [1,2,3,4]
let arrClone = arr.slice() //take the element of the old array an put in a new one


