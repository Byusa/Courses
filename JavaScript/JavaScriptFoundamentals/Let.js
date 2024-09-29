// The let keyword was introduced in ES6 (2015).
//1) Variables defined with let:
    // A) Cannot be Redeclared.
    let x = "John Doe";
    // let x = 0; // this can not be done

    // B) Must be Declared before use.

    // C) Variables defined with let have Block Scope.

//2) Block Scope
// before we had Global and functional scope 
// but let and const we only have block scope
{
    let x = 2;
}
// x can NOT be used here

// does not apply with var
{
    var x = 2;
  }
  // x CAN be used here

//3) Redeclaring Variables
// var
var p = 10;
// Here p is 10

{
var p = 2;
// Here x is 2
}

// Here p is 2

// let
let l = 10;
// Here l is 10

{
let l = 2;
// Here l is 2
}

// Here l is 10


// 4) Let Hoisting
carName = "Volvo";
var carName;
console.log(carName)

// this not done with let
carName2 = "Volvo";
let carName2;
console.log(carName2)

