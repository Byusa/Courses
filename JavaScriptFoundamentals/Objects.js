// 1. Object Literal Syntax
const car  = {
    model: "Range Rover",
    brand: "LandRover Evoque",
    year: 2015,
    color:"gray"
}
console.log(car)

//2. new object
const car2 = new Object()
car2.model = "Toyota";
car2.brand = "Corola";
car2.year = 2024;
car2.color = "Red";
console.log(car2)

//3. using constructor function
// for creating mulitple objects of the same structure
function MyCar(model, brand, year, color){
    this.model = model;
    this.brand = brand; 
    this.year = year; 
    this.color = color; 
}

const myCar = new MyCar("Suzuki", "Vitara", 2021, "White");
console.log(myCar)

//4. using ES6 Classes
// Modern and prefered way of creating classes in js
class MyCar2{
    constructor(model, brand, year, color, owner){
        this.model = model;
        this.brand = brand; 
        this.year = year; 
        this.color = color; 
        this.owner = owner;
    }
}
const myCar2 = new MyCar2("Land Rover", "Range Rover Evoque", 2015, "Gray", "Serge");
console.log(myCar2)

//5. Accessing Object Propertie
// Dot notation
console.log(myCar2.color);

//bracket notation (when property name is dynamic)
console.log(myCar2["color"]);

const prop =  "color"
console.log(myCar2[prop])

//6. Modify object Propeties
// You can add, update or delete properties in an object. 
// Adding or updating Propeties
myCar2.year = 2024
myCar2.color = "Black"
console.log(myCar2)

//Deleting Properties
delete myCar2.color
console.log(myCar2)
console.log(myCar2.color) //undefined

// lets recreate it
myCar2.color = "Black"
console.log(myCar2)

//7. Commonly Used Object Methods
//7.1 Object.values()
const keys = Object.keys(myCar2);
console.log(keys);

//7.2 Object.values()
const values = Object.values(myCar2);
console.log(values);

//7.3 Object.entries()
const entries = Object.entries(myCar2);
console.log(myCar2);

//7.4 Object.assign()
// Shallow copy or merging objects
const additionalInfo = {price: 45000, location: "Vancouver"}
const updatedCar  =  Object.assign({}, myCar2, additionalInfo)
console.log("Merging");
console.log(updatedCar);
console.log("Shallow copy");
const shallowCopy  =  Object.assign({}, myCar2);
console.log(shallowCopy.color, myCar2.color);// both are black
console.log("Deep copy");
const deepCopy  =  JSON.parse(JSON.stringify(myCar2));
deepCopy.color = "Pink"
console.log(deepCopy.color, myCar2.color); // Pink, Black

// Deep copy


//7.5 Object.freezer()
// Freezes an object, preventing any modifications (adding, deleting, or updating properties)
const freezeCar = Object.freeze(myCar2)
delete myCar2.color;
console.log(myCar2.color); // Black it was not deleted

// 7.6 Object.seal()
//prevnet deleting it but allows to modify it
const sealedCar = Object.seal(myCar)
delete myCar.color;
console.log(myCar.color); // white it was not deleted
myCar.color = "gray";
console.log(myCar.color); // gray it was not deleted


//8. Working with nested Objects 
// Objects that contains other objects (complex structure)
const person = {
    name: "Serge",
    age: 30,
    address:{
        street: "2288 Alpha Avenue", 
        city: "Burnaby",
        country: "Canada"
    }
}; 

console.log(person.address.city);

// 9. Object destructuring 
// Destructuring allows you to extract properities from an object into variables
const {name, age} = person;
console.log(name, age);
const {street, city} = person.address;
console.log(street, city);

//10. Spread Operator with Objects
// The spread operator(`...`) allows you to create a new object 
// by copying properties from an existing object
console.log(myCar); // { model: 'Suzuki', brand: 'Vitara', year: 2021, color: 'gray' }
const newCar = {...myCar, color: "red"}
console.log(newCar); // { model: 'Suzuki', brand: 'Vitara', year: 2021, color: 'red' }

// 11. Looping through Objects
// You can loop through an object using 
// for ...in  
// with Object.keys() in combination with forEach()
// 11. a) for ...in
for ( let key in myCar){
    //key
    //myCar[key]
    console.log(`${key}: ${myCar[key]}`)
}
// 11. b) Object.keys() and forEach
Object.keys(myCar).forEach(key => {
    //key
    //myCar[key]
    console.log(`${key}: ${myCar[key]}`);
});


// 12. Prototypes (objects) and inheritance
// Every javascript object has a prototype, which is also an object.
// Prototypes are used to properties and methods to an object, 
// Which can be inherited by other objects

// 12. A) Adding methods to a constructor function's prototype
MyCar2.prototype.start = function(){
    console.log(`${this.brand} ${this.model} is starting`)
}
myCar2.start();


