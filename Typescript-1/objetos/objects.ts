(() =>{
    let falsh: {name:string, age?:number, powers: string[],getName?: () => string} = {
        name: "Barry",
        age: 25,
        powers: ['Velocidad' , 'Salto']
    };

    falsh = {
        name: 'Pepe',
        age: 23,
        powers: ['Fuerza'],
        getName(){
            return this.name;
        }
    }

    console.log({falsh});
})()