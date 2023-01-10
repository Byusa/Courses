let a = true
let num = 0

let id = setInterval(() => {
    console.log(num++) // prints up to 8
}, 200) // print a every two second

setTimeout(()=> {
    clearInterval(id) // will let the cursor free after 2 sec
}, 2000) // after 2 sec a = false



// while(a){
//     console.log(num++) // the thread is never free to let setTimeout give results
// }
