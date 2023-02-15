// Arrow functions
const myFunc = function funcName(name){
    console.log("Hey", name)
}
myFunc("Serge, this is not arrow function")
//that becomes this
const callMeA =(name)=>{
    console.log("Hey", name)
}

myFunc("Byusa, this is arrow function")

// No argument
const callMeNo = () => {
    console.log("No args")
}
callMeNo()
// One arg
const callMeArg = name => {
    console.log("One arg ", name)
}

callMeArg("Serge")


// Just returning a value 
const callMeReturn = name => {
    return name
}
console.log(callMeReturn("Serge"))

//also could be 
const callMeReturn2 = name => name
console.log(callMeReturn("Byusa"))

