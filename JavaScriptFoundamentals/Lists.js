const hotels = [
    {
        id: 1,
        name: "Sheraton Dallas Hotel",
        address: {
            street: "1234 Main St",
            city: "Dallas",
            state: "TX",
            zip: "75201"
        },
    },
    {
        id: 2,
        name: "Miami Hilton",
        address: {
            street: "1234 Dubbo St",
            city: "Miami",
            state: "FL",
            zip: "75201"
        },
    },
    {
        id: 3,
        name: "Miami Hilton",
        address: {
            street: "1234 Dubbo St",
            city: "Miami",
            state: "FL",
            zip: "75201"
        },
    },
];

// 1) find the first hotel with the name "Miami Hilton"
const hotel = hotels.find(hotel => hotel.name === "Miami Hilton");
console.log(hotel); // find the first with the name "Miami Hilton"

// 2) find all hotels with the name "Miami Hilton"
const hotelsWithSameName = hotels.filter(hotel => hotel.name === "Miami Hilton");
console.log(hotelsWithSameName); // find all with the name "Miami Hilton"

// 3) update object with id 2 to have the name "Miami Hilton Resort"
const hotelToUpdate = hotels.find(hotel => hotel.id === 2);
if (hotelToUpdate) {
    hotelToUpdate.name = "Miami Beach Hilton";
    hotelToUpdate.address.street = "5678 Ocean Dr";
}
console.log(hotelToUpdate); // update object with id 2 to have the name "Miami Hilton Resort"

// 4) add a new hotel to the list
const newHotel = {
    id: 4,
    name: "Miami Hilton Resort",
    address: {
        street: "1234 Dubbo St",
        city: "Miami",
        state: "FL",
        zip: "75201"
    },
};

hotels.push(newHotel);
console.log(hotels); // add a new hotel to the list

// 5) Deleting or remove the hotel with id 1 from the list  
const hotelToRemove = hotels.find(hotel => hotel.id === 1);
if (hotelToRemove) {
    hotels.splice(hotels.indexOf(hotelToRemove), 1);
}
console.log(hotels); // remove the hotel with id 1 from the list

// 6) Deleting an object from a list
const hotelToDelete = 1;
const updatedHotels = hotels.filter(hotel => hotel.id !== hotelToDelete);

// 7) Mapping over a objects in a list
const hotelNames = hotels.map(hotel => hotel.name);
console.log(hotelNames); // mapping over a objects in a list
// output: [ 'Sheraton Dallas Hotel', 'Miami Beach Hilton', 'Miami Hilton Resort' ]

//8) Finding an object by a Nested Property
const hotelInMiami = hotels.find(hotel => hotel.address.city === "Miami");
console.log(hotelInMiami); // find the first hotel in Miami

//9) Checking if any object matches a condition
const hasHotelInTaxas = hotels.some(hotel => hotel.address.state === "TX");
console.log(hasHotelInTaxas); // check if any hotel is in Texas
//output: true

//10) checking if all objects match a condition
const allHotelsInFL = hotels.every(hotel => hotel.address.state === "FL");
console.log(allHotelsInFL); // check if all hotels are in Florida
//output: false

//11) Sorting a list of objects
const sortedHotels = hotels.sort((a, b) => a.name.localeCompare(b.name));
console.log(sortedHotels); // sort the hotels by name

//12) Reducing a list of objects to a single value
const totalHotels = hotels.reduce((total, hotel) => total + 1, 0);
console.log(totalHotels); // count the total number of hotels
//output: 3

//13) Adding/Updating Properties in Objects
const user = { name: "John Doe", age: 30 };
const updatedUser = { ...user, age: 31, city: "New York" };
console.log(updatedUser); // add/update properties in objects
