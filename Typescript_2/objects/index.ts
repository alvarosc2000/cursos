/** 
 * Types
 */

type Post = {
    title: string,
    content: string,
    date: Date
}


/**
 * Optional --> ?
 */
type Author = {
    name ?: string,
    age: number,
    email: string
}

type Post1 = {
    title: string,
    content: string,
    date: Date,
    author: Author
}

type AwardsDetails = {
    name: string,
    date: Date
}

type Awards = {
    [key: string]: AwardsDetails
}

type Post2 = {
    title: string,
    content: string,
    date: Date,
    author: Author,
    awards: Awards
}

type Dog = {
    name: string,
    barks: boolean,
    wags: boolean
};

type Cat = {
    name: string,
    purrs: boolean,
}

type DogAndCatUnion = Dog|Cat

/**
*   Union 
*/ 

type HybridAnimal = Dog & Cat

/** 
 * Simple objects
 */

let person = {
    name: "Mark",
    age: 32
}

let car: Object = {
    brand: "BMW",
    color: "Black"
}

// Reassignments
car = [];
car = () => {};

let newCar: {
    brand: string,
    color: string
} = {
    brand: "BMW",
    color: "Black"
}


/**
 * Posts
 */

let post: Post = {
    title: "This is a blog post",
    content: "Content of the post",
    date: new Date()
}

let post1: Post1 = {
    title: "This is a blog post",
    content: "Content of the post",
    date: new Date(),
    author: {
        name: "John",
        age: 23,
        email: "john@gmail.com"
    }
}

let post2: Post2 = {
    title: "This is a blog post",
    content: "Content of the post",
    date: new Date(),
    author: {
        name: "John",
        age: 23,
        email: "john@gmail.com"
    },
    awards: {
        web: {
            name: "Web awards",
            date: new Date()
        },
        web3: {
            name: "Web awards",
            date: new Date()
        }
    }
}


let dog: DogAndCatUnion = {
    name: "Buddy",
    barks: true,
    wags: true,
}

let cat: DogAndCatUnion ={
    name: "Bella",
    purrs: true,
}


let hybridAnimal: HybridAnimal = {
    name: "DOG",
    barks: true,
    wags: true,
    purrs: false
};


/**
 * Ejercicio
 */

// Define union types for theme and language
type Theme = "light" | "dark";
type Language = "English" | "Spanish";

// Define the User type alias
type User_e = {
    readonly id: number;             // read-only unique identifier
    name: string;                    // user's name
    age?: number;                    // optional age
    contact: {                       // nested contact object
        email: string;               // required email
        phone?: string;              // optional phone
    };
    preferences: {                   // nested preferences object
        theme: Theme;                // 'light' | 'dark'
        language: Language;          // 'English' | 'Spanish'
    };
    [key: string]: any;              // index signature for additional properties
}

// Create the user object with proper initializations
let user_e: User_e = {
    id: 1,                                // read-only number
    name: "John Doe",
    contact: {
        email: "john@example.com",        // required email
        // phone is optional and not initialized
    },
    preferences: {
        theme: "dark",
        language: "English"
    },
    additionalInfo: "This is an example of an index signature property"
    // other dynamic properties could be added here because of the index signature
}

