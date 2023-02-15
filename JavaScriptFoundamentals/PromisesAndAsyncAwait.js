// Promise object represents the eventual completion (or failure) of an asynchronous operation and its resulting value.
const axiosRequest = require('axios')

async function getActivity(){
    try{
        let response = await axiosRequest.get("https://www.boredapi.com/api/activity")
        console.log(`You could ${response.data.activity}`)
    } catch (error) {
        console.error(`ERROR! ${error}`)
    }

}
getActivity()
//bad way to do it
//  axiosRequest.get("https://www.boredapi.com/api/activity")
//     .get('https://httpstatus/404')
//     .then(response => {
//         console.log(`You could ${response.data.activity}`)
//     })
//     .catch(error => {
//         console.error(`ERROR! ${error}`)
//     })

// console.log("Why am I here?")