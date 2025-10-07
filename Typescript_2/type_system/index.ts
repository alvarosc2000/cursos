/**
 * Any
 */

let firstname_1: any = "Mark";
firstname_1 = [];
firstname_1 = 123;


/**
 * Unknown types
 */

function multiplyByTwo(number:unknown){
    if (typeof number === "number"){
        return number * 2;
    }
    return "Please provide a valid number";
}

console.log(multiplyByTwo(2));


/**
 * Alias
 */

//Declaration
type CustomString = string;
type CustomNumber = number;
type CustomDate = Date;
type CustomSymbol = Symbol;

//Annotation
let firstName_2: CustomString = "Pepe";
let age_2: CustomNumber = 23;
let today: CustomDate = new Date();
let unique_2: CustomSymbol = Symbol();


function addNumber(a:number, b:number){
    return a+b;
}

//Inference
let finalResult = addNumber(10,15);



/**
 * Union
 */

type StringOrNumber = string | number;

let StringOrNumber = 1232;

function print(input: string| undefined){
    if (input){
        console.log(input);
    }
    console.log("Please input something to print");
}


/**
 * Conditional types
 */

type TrueString= CustomString extends string ? true: false;

/**
 * Casting
 */

let firstname_3 = <any> "Mark";
let lastName = "Doe" as any;

let user_3 = {
    name: "Mark",
    email : "mark@email.com"
};

type User = {
    name: string,
    email: string
}


function fetchUser(){
    return user_3 as User;
}

const fetched_user = fetchUser();


// 1️⃣ Define un conditional type IsStringType
type IsStringType<T> = T extends string ? boolean : number;

// 2️⃣ Declara typeCheck usando IsStringType
// Si el tipo es string, será boolean, si no, number
let typeCheck: IsStringType<string> = true;  // como usamos string, es boolean

// Si lo probamos con otro tipo, por ejemplo number:
// let typeCheckNumber: IsStringType<number> = 0;

// 3️⃣ Crea anyValue de tipo any
let anyValue: any = "example";

// 4️⃣ Haz type assertion para string
let castValue: string = anyValue as string;

console.log(typeCheck);  // true
console.log(castValue);  // "example"
