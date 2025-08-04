"use strict";
(function () {
    var name = "Alvaro";
    function returnName() {
        return name;
    }
    var cambiarNombre = function () {
        return 'Juan';
    };
    console.log(typeof returnName);
    console.log(typeof cambiarNombre);
})();
