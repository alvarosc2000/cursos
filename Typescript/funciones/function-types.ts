(() =>{

    const addNumber = (a:number, b:number) => a+b;
    const greet = (name:string) => `Hola ${name}`;
    const save = () => 'Salvando...';


    let myFunction;

    myFunction = 10;
    console.log(myFunction);

    myFunction = addNumber;
    console.log(myFunction(1,2));

    myFunction = greet;
    console.log(myFunction('Pedro'));

    myFunction = save;
    console.log(myFunction());
})()