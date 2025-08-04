"use strict";
(function () {
    var fullName = function (firstName) {
        var restArg = [];
        for (var _i = 1; _i < arguments.length; _i++) {
            restArg[_i - 1] = arguments[_i];
        }
        return "".concat(firstName, " ").concat(restArg.join(' '));
    };
    var superman = fullName('Pepe', 'Juan', 'Curro');
    console.log({ superman: superman });
})();
