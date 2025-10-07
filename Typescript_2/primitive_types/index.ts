/**
 *  Usa let si necesitas una variable que cambie.
    Usa const por defecto, cuando no quieras que la referencia cambie.
    Evita var, ya que puede causar errores por su alcance y hoisting.
 */


/**
 * String types
 */

var firstname: string = "John";
let automovile = "AUDI";
const city = "Malaga";
let students = 32;
let studentsAsString:  string = students.toString();


/**
 * Number types
 */

var age: number = 32;
let year: number = 2025;
const numberOfmenbers = 61;
let stringToNumer: number = parseInt("1988")


/**
 * Booleans
 */

let isStudent: boolean = false;
const alwaysStudent = true;
let minimumAge = age >= 6 ? true: false;


/**
 * Null and undefined
 */

let fetched: null = null;
let user: undefined = undefined;

/**
 * Bigint
 */

let largeNumber: bigint = 98451651894n;

/**
 * Symbol
 */

let unique: symbol = Symbol("uniqueSymbol")