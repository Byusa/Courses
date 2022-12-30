// Destructing 
// Allow you to easily access the values of arrays and objects and assign them to variables
// eg: Destructing an Arrays
const array = [ 1, 2, 3 ]
const [ a, b ] = array
console.log(a)
console.log(b)

// eg: Destructing an object
const myObj = {
    name: "Byusa",
    age: 29 
}
const { name } = myObj
console.log(name)
// console.log(age) // undefined
const { age } = myObj
console.log(age)

// Destruction is very useful when working with function arguments. 
// eg: 
const printName = (personObj) => {
    console.log(personObj.name)
}
printName({name: 'Serge', age: 29})

// Same code as above but condensed
const printName2 = ({name}) => {
    console.log(name)
}
printName({name: 'Serge', age: 29})
