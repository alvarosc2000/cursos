/**
 * Any
 */
var firstname_1 = "Mark";
firstname_1 = [];
firstname_1 = 123;
/**
 * Unknown types
 */
function multiplyByTwo(number) {
    if (typeof number === "number") {
        return number * 2;
    }
    return "Please provide a valid number";
}
console.log(multiplyByTwo(2));
