let a = true
setTimeout(()=> {
    a = false;
}, 2000) // after 2 sec a = false

// setInterval(() => {
//     if(a) {
//         console.log('Hello')
//     }
// }, 200) // print a every two second

while(a){
    console.log("sup")
}