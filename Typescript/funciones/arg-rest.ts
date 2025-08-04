(() => {

    const fullName = (firstName: string, ...restArg:string[]):string =>{
        return `${firstName} ${restArg.join(' ')}`
    }

    const superman  = fullName('Pepe', 'Juan', 'Curro');


    console.log({superman});

})()