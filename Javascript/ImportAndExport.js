// Imports and Export
// Files are called modules

// Two different types of exports
// default(unnamed) and namedexports
// 1) default => export default ...;
// 2) named => export const someData = ....;

// imports
// 1) default => someNameOfYourChoice could be any name 
// import someNameOfYourChoice from './path/to/files.js'

// 2) same name as exported
// import { someData } from './path/to/files.js'
// you can import all
// import * from './path/to/files.js'

// UptoYOU bundle all 
// export const someData = ....
// UptoYOU.someData

// Classes 
// old JS
class Person {
    constructor(){
        this.name = "Serge"
    }
}

const p  = new Person()
console.log(p.name)

// New JS

class Person2 {
    name = "serge"
}
const p2  = new Person()
console.log(p2.name)

// More
class Person3 {
    name = "serge";
    printName (){
        console.log(this.name)
    }
}
const p3  = new Person3()
p3.printName()

// Or like this
class Person4 {
    name = "serge";
    printName = ()=> {
        console.log(this.name)
    }
}
const p4  = new Person4()
p4.printName()

// inheritance
class Human {
    spicies = "Human";
}
class Person7 extends Human {
    name = "Byusa";
    printMyName = () => {
        console.log(this.name);
    }
}
const p7 = new Person7();
p7.printMyName();
console.log(p7.spicies)






