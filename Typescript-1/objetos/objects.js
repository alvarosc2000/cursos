"use strict";
(function () {
    var falsh = {
        name: "Barry",
        age: 25,
        powers: ['Velocidad', 'Salto']
    };
    falsh = {
        name: 'Pepe',
        age: 23,
        powers: ['Fuerza'],
        getName: function () {
            return this.name;
        }
    };
    console.log({ falsh: falsh });
})();
