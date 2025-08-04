(() =>{
    const numbers: (string | number | boolean)[] = [1,2,3,4,5,6,7,8,9,19];
    const texto = ['alv', 'bal', 'calv'];
    numbers.push(23);
    numbers.push("23");
    numbers.push(true);

    console.log(numbers);

    texto.forEach(v => console.log(v.toUpperCase()))

})()