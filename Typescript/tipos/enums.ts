(() => {

    enum AuidoLevel {
        min = 1,
        medium,
        max= 10,
    }

    let currentAudio:AuidoLevel = AuidoLevel.max;

    console.log(currentAudio);
    console.log(AuidoLevel);

})()