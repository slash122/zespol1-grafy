function seqGraphDisplay(response, exceptionContanierId) {
    let data = JSON.parse(response)
    let exceptionContanier = document.getElementById(exceptionContanierId);

    exceptionContanier.innerHTML = `<div class="alert alert-success" style="margin-top: 10px" role="alert">Operacja skończyła się sukcesem. 
    Wykres grafu jest na dole.</div>`;
    let img = data.graphImage;

    document.getElementById("graphImage").src = "data:image/png;base64," + img;
}


function processGraphicSeq() {
    let graphSequence = document.getElementById("graphicSequenceInput").value;

    $.ajax({
        type: "POST",
        url: "/zestaw2/graphicseq",
        data: {
            graphSequence: graphSequence,
        },
        success: function (response) {
            seqGraphDisplay(response, "sequenceExceptionContainer")
        },
        error: function (response) {
            let exceptionContanier = document.getElementById("sequenceExceptionContainer");
            let exceptionMsg = JSON.parse(response.responseText).exceptionMsg;
            exceptionContanier.innerHTML = `<div class="alert alert-danger" style="margin-top: 10px" role="alert">${exceptionMsg} </div>`;
        }
    });
}


function processRandGraphicSeq() {
    let randGraphSequence = document.getElementById("randGraphicSequenceInput").value;
    let randVal = document.getElementById("randValInput").value;

    $.ajax({
        type: "POST",
        url: "/zestaw2/randgraphicseq",
        data: {
            graphSequence: randGraphSequence,
            randVal: randVal
        },
        success: function (response) {
            seqGraphDisplay(response, "randSequenceExceptionContainer")
        },
        error: function (response) {
            let exceptionContanier = document.getElementById("randSequenceExceptionContainer");
            let exceptionMsg = JSON.parse(response.responseText).exceptionMsg;
            exceptionContanier.innerHTML = `<div class="alert alert-danger" style="margin-top: 10px" role="alert">${exceptionMsg} </div>`;
        }
    });
}


function processCohesive() {
    let adjacencyList = document.getElementById("cohesiveCode").value;

    $.ajax({
        type: "POST",
        url: "/zestaw2/cohesive",
        data: {
            adjacencyList: adjacencyList,
        },
        success: function (response) {
            let data = JSON.parse(response);
            let exceptionContanier = document.getElementById("cohesiveExceptionContainer");

            exceptionContanier.innerHTML = `<div class="alert alert-success" style="margin-top: 10px" role="alert">Operacja skończyła się sukcesem.` 
            document.getElementById("cohesiveResult").innerHTML = data.maxCohesive;
        },
        error: function (response) {
            let exceptionContanier = document.getElementById("cohesiveExceptionContainer");
            let exceptionMsg = JSON.parse(response.responseText).exceptionMsg;
            exceptionContanier.innerHTML = `<div class="alert alert-danger" style="margin-top: 10px" role="alert">${exceptionMsg} </div>`;
            document.getElementById("cohesiveResult").innerHTML = "";
        }
    });
}


function processEuler() {
    let randNum = document.getElementById("eulerRandNum").value;
    
    $.ajax({
        type: "POST",
        url: "/zestaw2/euler",
        data: {
            randNum: randNum,
        },
        success: function (response) {
            let data = JSON.parse(response);
            let exceptionContanier = document.getElementById("eulerExceptionContainer");

            exceptionContanier.innerHTML = `<div class="alert alert-success" style="margin-top: 10px" role="alert">Operacja skończyła się sukcesem.` 
            document.getElementById("eulerMatrixResult").innerHTML = data.adjMatrix;
            document.getElementById("eulerPathResult").innerHTML = data.path;

            document.getElementById("graphImage").src = "data:image/png;base64," + data.graphImage;
        },
        error: function (response) {
            let exceptionContanier = document.getElementById("eulerExceptionContainer");
            let exceptionMsg = JSON.parse(response.responseText).exceptionMsg;
            exceptionContanier.innerHTML = `<div class="alert alert-danger" style="margin-top: 10px" role="alert">${exceptionMsg} </div>`;
            document.getElementById("eulerMatrixResult").innerHTML = "";
            document.getElementById("eulerPathResult").innerHTML = "";
        }
    });
}


function processRandomKRegular() {
    let param1 = document.getElementById("randomKRegularParam1").value;
    let param2 = document.getElementById("randomKRegularParam2").value;

    $.ajax({
        type: "POST",
        url: "/zestaw2/randomkregular",
        data: {
            param1: param1,
            param2: param2,
        },
        success: function (response) {
            let data = JSON.parse(response);
            let exceptionContanier = document.getElementById("randomKRegularExceptionContainer");

            exceptionContanier.innerHTML = `<div class="alert alert-success" style="margin-top: 10px" role="alert">Operacja skończyła się sukcesem.
            Wykres grafu jest na dole.` 
            document.getElementById("graphImage").src = "data:image/png;base64," + data.graphImage;
        },
        error: function (response) {
            let exceptionContanier = document.getElementById("randomKRegularExceptionContainer");
            let exceptionMsg = JSON.parse(response.responseText).exceptionMsg;
            exceptionContanier.innerHTML = `<div class="alert alert-danger" style="margin-top: 10px" role="alert">${exceptionMsg} </div>`;
            document.getElementById("randomKRegularResult").innerHTML = "";
        }
    });
}


function processHamilton() {
    let randNum = document.getElementById("eulerHamiltonRandNum").value;

    $.ajax({
        type: "POST",
        url: "/zestaw2/hamilton",
        data: {
            randNum: randNum,
        },
        success: function (response) {
            let data = JSON.parse(response);
            let exceptionContanier = document.getElementById("eulerExceptionContainer");

            exceptionContanier.innerHTML = `<div class="alert alert-success" style="margin-top: 10px" role="alert">Operacja skończyła się sukcesem.` 
            document.getElementById("hamiltonPathResult").value = data.path;

            document.getElementById("graphImage").src = "data:image/png;base64," + data.graphImage;
        },
        error: function (response) {
            let exceptionContanier = document.getElementById("eulerExceptionContainer");
            let exceptionMsg = JSON.parse(response.responseText).exceptionMsg;
            exceptionContanier.innerHTML = `<div class="alert alert-danger" style="margin-top: 10px" role="alert">${exceptionMsg} </div>`;
            document.getElementById("hamiltonPathResult").value = '';
        }
    });
}