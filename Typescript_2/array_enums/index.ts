let a:number[] = [1,2,3];
let b: Array<string> = ["a","b","c"];
let c:(string|number|boolean)[] = ["a",2, true]

type Seats = {
    [keyof: string]: string;
};

type Caterer = {
    name: string,
    address: string,
    phone: number;
};

type Airplane ={
    model: string,
    flightNumber: string;
    timeOfDeparture: Date;
    timeOfArrival: Date;
    caterer: Caterer;
    seats: Seats;
};


type Airplanes=  Airplane[];


let airplane: Airplanes =[
    {
    model: "Airbus A380",
    flightNumber: "A2210",
    timeOfDeparture: new Date(),
    timeOfArrival: new Date(),
    caterer:{
        name: "Special Food Ltd",
        address: "484, Some Street, New York",
        phone: 7867859751,
    },
    seats:{
        A1: "John Doe",
        A2: "Mark Deo",
        A3: "Sam Doe",
    },
}
];



/**
 * Tuples
 */