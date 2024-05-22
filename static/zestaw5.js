function processResponse(response) {
    let data = JSON.parse(response);
    let exceptionContanier = document.getElementById("exceptionContainer");
    
    exceptionContanier.innerHTML = `<div class="alert alert-success" style="margin-top: 10px" role="alert">Operacja skończyła się sukcesem. </div>`;

    let layeredImg = data.layeredImg;
    document.getElementById("graphLayeredImage").src = "data:image/png;base64," + layeredImg;

    let circleImg = data.circleImg;
    document.getElementById("graphCircularImage").src = "data:image/png;base64," + circleImg;

    document.getElementById("maxFlow").value = data.maxFlow;
}


function processNetwork() {
    let layerNum = document.getElementById("layerInput").value;

    $.ajax({
        type: "POST",
        url: "/zestaw5/process",
        data: {
            layerNum: layerNum
        },
        success: function (response) {
            processResponse(response)
        },
        error: function (response) {
            let exceptionContanier = document.getElementById("exceptionContainer");
            let exceptionMsg = JSON.parse(response.responseText).exceptionMsg;
            exceptionContanier.innerHTML = `<div class="alert alert-danger" style="margin-top: 10px" role="alert">${exceptionMsg} </div>`;
        }
    });
}