"use strict";
(function () {
    var addNumber = function (a, b) { return a + b; };
    var greet = function (name) { return "Hola ".concat(name); };
    var save = function () { return 'Salvando...'; };
    var myFunction;
    myFunction = 10;
    console.log(myFunction);
    myFunction = addNumber;
    console.log(myFunction(1, 2));
    myFunction = greet;
    console.log(myFunction('Pedro'));
    myFunction = save;
    console.log(myFunction());
})();
