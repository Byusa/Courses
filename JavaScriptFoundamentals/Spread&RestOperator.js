// Spread and Rest Operators
// ... spread and Rest operators use the same syntax

// 1) Using the Spread Opearator
// Spread operator allows you to:
// pull the elements out of the array (split into a list of elements)
// eg:
const oldArray = [1,2,3]
const newArray = [...oldArray, 4,5,6]
console.log(newArray)
// so useful in cloning an array (since both are refference types)
const cloneOldArray = [...oldArray] // Shallow copy
console.log(cloneOldArray)
if(oldArray===cloneOldArray){
    console.log("True")
}else{
    console.log("False")
    if(oldArray==cloneOldArray){
        console.log("True")
    }else{
        console.log("False")
    }
}

// or pull the properites out of an object 
const oldObject = {
    name : "Byusa"
}
const newObject = {
    ...oldObject,
    age : 29
}
console.log(newObject)