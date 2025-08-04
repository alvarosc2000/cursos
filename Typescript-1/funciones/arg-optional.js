"use strict";
(function () {
    var fullName = function (firstName, lastName) {
        return "".concat(firstName, " ").concat(lastName || 'no last name');
    };
    var name = fullName('Alvaro');
    console.log({ name: name });
})();
