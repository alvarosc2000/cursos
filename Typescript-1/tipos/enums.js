"use strict";
(function () {
    var AuidoLevel;
    (function (AuidoLevel) {
        AuidoLevel[AuidoLevel["min"] = 1] = "min";
        AuidoLevel[AuidoLevel["medium"] = 2] = "medium";
        AuidoLevel[AuidoLevel["max"] = 10] = "max";
    })(AuidoLevel || (AuidoLevel = {}));
    var currentAudio = AuidoLevel.max;
    console.log(currentAudio);
    console.log(AuidoLevel);
})();
