(() =>{

    const name:string = "Alvaro";

    function returnName():string{
        return name;
    }

    const cambiarNombre = ():string =>{
        return 'Juan';
    }

    console.log(typeof returnName);
    console.log(typeof cambiarNombre);

})()