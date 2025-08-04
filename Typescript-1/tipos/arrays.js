"use strict";
(function () {
    var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 19];
    var texto = ['alv', 'bal', 'calv'];
    numbers.push(23);
    numbers.push("23");
    numbers.push(true);
    console.log(numbers);
    texto.forEach(function (v) { return console.log(v.toUpperCase()); });
})();
